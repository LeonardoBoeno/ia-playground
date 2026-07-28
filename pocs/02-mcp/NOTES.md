# Study notes — Phase 2 (MCP)

- Host = the app talking to the LLM (Claude Desktop, Claude Code).
- Client = lives inside the host, holds one connection to one server.
- Server = this process. Exposes Tools (callable), Resources (readable data), Prompts (templates).
- Transport used here: stdio (the default for local servers launched by the host).

This file is served back to the model via the `notes://study` Resource in server.py,
as a way to test that Resources work end-to-end.
