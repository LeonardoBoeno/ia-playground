from pathlib import Path

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


@mcp.resource("notes://study")
def study_notes() -> str:
    """Expose this POC's NOTES.md as an MCP Resource."""
    notes_path = Path(__file__).parent / "NOTES.md"
    return notes_path.read_text()


if __name__ == "__main__":
    mcp.run()
