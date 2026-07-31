from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("study-mcp-poc")

# A tiny in-memory lookup so get_weather doesn't need a geocoding API key.
CITY_COORDS = {
    "sao paulo": (-23.55, -46.63),
    "rio de janeiro": (-22.91, -43.17),
    "new york": (40.71, -74.01),
    "london": (51.51, -0.13),
}


@mcp.tool()
def get_weather(city: str) -> str:
    """Get the current temperature for a known city.

    Args:
        city: City name (e.g. "Sao Paulo", "London").
    """
    key = city.strip().lower()
    if key not in CITY_COORDS:
        known = ", ".join(sorted(CITY_COORDS))
        return f"Unknown city '{city}'. Known cities: {known}"

    lat, lon = CITY_COORDS[key]
    resp = httpx.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": lat, "longitude": lon, "current": "temperature_2m"},
        timeout=10.0,
    )
    resp.raise_for_status()
    data = resp.json()
    temp = data["current"]["temperature_2m"]
    unit = data["current_units"]["temperature_2m"]
    return f"Current temperature in {city.title()}: {temp}{unit}"


# Real coastal spots (lat/lon of the beach itself, not a city center) — separate
# from CITY_COORDS above because most of those aren't surfable at all.
SURF_SPOTS = {
    "atalaia": (-26.91, -48.38),
    "copacabana": (-22.97, -43.19),
    "bondi beach": (-33.89, 151.27),
}


@mcp.tool()
def check_surf_conditions(spot: str, date: str) -> str:
    """Check surf conditions for a known surf spot at a given hour.

    Args:
        spot: Surf spot name (e.g. "Atalaia", "Copacabana", "Bondi Beach").
        date: Either the literal "now", or an exact hourly timestamp in
            "YYYY-MM-DDTHH:00" LOCAL time for that spot, within the next ~7
            days (e.g. "2026-08-01T09:00"). For requests like "tomorrow at
            9am", work out the date yourself (you know today's date) and
            pass the resulting timestamp - this tool only resolves "now".
    """
    key = spot.strip().lower()
    if key not in SURF_SPOTS:
        known = ", ".join(sorted(SURF_SPOTS))
        return f"Unknown spot '{spot}'. Known spots: {known}"

    lat, lon = SURF_SPOTS[key]
    resp = httpx.get(
        "https://marine-api.open-meteo.com/v1/marine",
        params={
            "latitude": lat,
            "longitude": lon,
            "hourly": "wave_height,wave_direction,wave_period,wind_wave_height,wind_wave_direction,sea_surface_temperature",
            "forecast_days": 7,
            "timezone": "auto",
        },
        timeout=10.0,
    )
    resp.raise_for_status()
    data = resp.json()

    # "now" is only meaningful once we know which timezone this spot is in -
    # Open-Meteo tells us via data["timezone"] (e.g. "America/Sao_Paulo"),
    # matching timezone=auto above. Floor to the current hour to match the
    # hourly step size.
    if date.strip().lower() == "now":
        now_local = datetime.now(ZoneInfo(data["timezone"]))
        lookup = now_local.strftime("%Y-%m-%dT%H:00")
    else:
        lookup = date

    hourly = data["hourly"]
    if lookup not in hourly["time"]:
        return (
            f"No forecast available for '{lookup}'. "
            f"Available range: {hourly['time'][0]} to {hourly['time'][-1]} (hourly steps, {data['timezone']})."
        )

    idx      = hourly["time"].index(lookup)
    wave_h   = hourly["wave_height"][idx]
    wave_d   = hourly["wave_direction"][idx]
    wave_p   = hourly["wave_period"][idx]
    wind_h   = hourly["wind_wave_height"][idx]
    wind_d   = hourly["wind_wave_direction"][idx]
    sea_temp = hourly["sea_surface_temperature"][idx]

    # --- your verdict thresholds ---
    good_height = 0.5 <= wave_h <= 1.2
    good_period = 7 <= wave_p <= 11
    low_chop = wind_h <= 0.3 * wave_h if wave_h > 0 else False
    good_temp = sea_temp >= 18

    checks_passed = sum([good_height, good_period, low_chop, good_temp])
    if checks_passed == 4:
        verdict = "Great - go surf!"
    elif checks_passed >= 2:
        verdict = "Decent, worth checking in person"
    else:
        verdict = "Not great, probably skip it"

    return (
        f"{spot} at {lookup}: {wave_h}m swell @ {wave_p}s from {wave_d}°, "
        f"{wind_h}m wind chop from {wind_d}°, sea temp {sea_temp}°C. "
        f"Verdict: {verdict}"
    )


@mcp.resource("notes://study")
def study_notes() -> str:
    """Expose this POC's NOTES.md as an MCP Resource."""
    notes_path = Path(__file__).parent / "NOTES.md"
    return notes_path.read_text()


if __name__ == "__main__":
    mcp.run()
