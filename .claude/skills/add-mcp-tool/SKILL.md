---
name: add-mcp-tool
description: Use when adding a new @mcp.tool() or @mcp.resource() to pocs/02-mcp/server.py, so the addition matches the file's existing conventions and the surrounding docs (README.md, NOTES.md, requirements.txt) stay in sync. Triggers on "add an MCP tool", "new tool for the MCP server", "add a resource to server.py", "extend the study-mcp-poc server".
---

# Adding a tool/resource to the study MCP server

`pocs/02-mcp/server.py` is a `FastMCP` server (`study-mcp-poc`) with an established style. Read the existing tools (`get_weather`, `check_surf_conditions`) before writing a new one — match their shape rather than inventing a new one.

## Conventions to follow

1. **Placement**: new tool/resource functions go above the `if __name__ == "__main__":` block at the bottom of the file.
2. **Decorator + signature**: `@mcp.tool()` on a function with type-annotated params and a `-> str` return. One tool = one function.
3. **Docstring**: one-line summary, blank line, then an `Args:` block. Each arg gets a short description and an example value in parentheses, e.g. `city: City name (e.g. "Sao Paulo", "London").` If a param takes a fuzzy/natural date or free text the model must resolve itself, spell out the exact format expected (see `check_surf_conditions`'s `date` arg) — don't leave format resolution ambiguous.
4. **Known-entity lookups**: if the tool only supports a fixed set of named things (cities, spots, etc.), back it with a module-level dict of `"lowercase name": (data...)` pairs, placed just above the function. If it's not obvious why a second lookup table is separate from an existing one, add a one-line comment explaining why (see the `SURF_SPOTS` vs `CITY_COORDS` split).
5. **Input validation**: normalize input with `.strip().lower()`, check membership in the lookup dict, and on a miss return a plain string error listing the known options via `", ".join(sorted(...))` — never raise for a bad user-supplied name.
6. **External calls**: use `httpx.get(url, params={...}, timeout=10.0)` then `resp.raise_for_status()` then `resp.json()`. Don't swallow HTTP errors — let `raise_for_status()` surface them.
7. **Return value**: a single human-readable string summarizing the result, not raw JSON or a dict.
8. **Resources**: use `@mcp.resource("scheme://name")` on a zero-or-simple-arg function returning a string, following `study_notes()`.

## After adding the tool

- If it needs a new dependency, add it (pinned, matching the `==` style already in `pocs/02-mcp/requirements.txt`).
- Update `pocs/02-mcp/README.md`'s "What's here" bullet list to mention the new tool/resource — this file already drifted out of sync once (it only lists `get_weather` even though `check_surf_conditions` exists), so don't let a new addition repeat that.
- If the change teaches something worth remembering about MCP itself (not just the POC), add a line to `pocs/02-mcp/NOTES.md` in its existing terse bullet style.
- Suggest the user sanity-check it with `mcp dev server.py` (MCP Inspector) or a quick in-process call before considering it done.
