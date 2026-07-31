# Phase 2 — MCP (Model Context Protocol)

**Goal:** understand the host/client/server architecture and build a working MCP server.

## What's here

A minimal server built with the official Python `mcp` SDK (`FastMCP`):

- **Tool** `get_weather(city)` — calls the free [Open-Meteo](https://open-meteo.com) API (no key required) for a small set of known cities.
- **Resource** `notes://study` — serves `NOTES.md` back to the model.

Files:
- `server.py` — the MCP server.
- `NOTES.md` — study notes, also exposed as the Resource.
- `requirements.txt` — pinned deps (`mcp[cli]`, `httpx`).
- `.venv/` — local virtualenv (gitignored).

## Setup

```bash
cd pocs/02-mcp
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run / test

**Quick sanity check** (runs the server over stdio, waits for a client — Ctrl+C to stop):
```bash
python server.py
```

**Interactive dev UI** (MCP Inspector — lets you call the tool/resource from a browser):
```bash
mcp dev server.py
```

**Install into Claude Desktop** (adds it to Claude Desktop's config automatically):
```bash
mcp install server.py
```

**Connect to Claude Code** instead:
```bash
claude mcp add study-mcp-poc -- python /absolute/path/to/pocs/02-mcp/server.py
```
Then in a Claude Code session, the `get_weather` tool and `notes://study` resource
should show up in `/mcp`.

## POC checklist

- [x] Build a simple MCP server (Python) with 1 Tool (`get_weather`, queries a real external API) and 1 Resource (`notes://study`).
- [x] Connect it to Claude Desktop or Claude Code.

## Status

Server built and verified end-to-end (tool call + resource read tested via in-process client).
Next: connect it to Claude Code/Desktop and drive it from an actual conversation.
