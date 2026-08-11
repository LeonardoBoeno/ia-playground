# AI Learning Roadmap: MCP, RAG, Agents & Local LLMs

> A sequential, hands-on study path to understand modern AI systems — from LLM fundamentals to MCP, RAG, multi-agent orchestration, evaluation, and running your own models locally.

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)

## About

This repo tracks my personal learning path through core AI engineering topics. Each phase includes curated readings, videos, reference repos, and a hands-on POC to validate the concept before moving on.

**Estimated time:** 9–12 weeks (part-time)

## Table of Contents

- [Phase 0 — AI/LLM Fundamentals](#phase-0--aillm-fundamentals)
- [Phase 1 — APIs & Prompt Engineering](#phase-1--apis--prompt-engineering)
- [Phase 2 — AI Gateways & AWS Bedrock](#phase-2--ai-gateways--aws-bedrock)
- [Phase 3 — MCP (Model Context Protocol)](#phase-3--mcp-model-context-protocol)
- [Phase 4 — Claude Skills, Commands & Rules](#phase-4--claude-skills-commands--rules)
- [Phase 5 — RAG (Retrieval-Augmented Generation)](#phase-5--rag-retrieval-augmented-generation)
- [Phase 6 — Running Models Locally](#phase-6--running-models-locally)
- [Phase 7 — Multi-Agent Systems](#phase-7--multi-agent-systems)
- [Phase 8 — Agent Evaluation & Benchmarks](#phase-8--agent-evaluation--benchmarks)
- [Phase 9 — Capstone Project](#phase-9--capstone-project)
- [Priority Order (Short on Time)](#priority-order-short-on-time)

---

## Phase 0 — AI/LLM Fundamentals
*(1–2 weeks)*

**Videos**
- [ ] 3Blue1Brown — *Neural Networks* series: [3blue1brown.com/topics/neural-networks](https://www.3blue1brown.com/topics/neural-networks)
- [ ] Andrej Karpathy — *Neural Networks: Zero to Hero* playlist (builds GPT from scratch in code)

**Repo**
- [ ] [karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero) — code for the playlist above

**Reading**
- [ ] [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — skim on first pass, don't get stuck on the math
- [ ] [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course) — free, hands-on

**POC**
- [ ] Implement a minimal Transformer (bigram → attention) notebook following Karpathy, just to internalize the mechanism.

---

## Phase 1 — APIs & Prompt Engineering
*(3–5 days)*

**Reading**
- [X] [Anthropic — Prompt Engineering Overview](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [X] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)

**POC**
- [ ] Script calling the Anthropic (or OpenAI) API with basic tool use / function calling — e.g., a small "agent" that queries a weather API.

---

## Phase 2 — AI Gateways & AWS Bedrock
*(3–5 days)*

Gateways sit between your app and one or more model providers: unified API, routing, fallback, caching, cost tracking, and observability across providers (cloud and local).

**Reading**
- [ ] [LiteLLM](https://github.com/BerriAI/litellm) — open-source, self-hosted gateway with an OpenAI-compatible API across 100+ providers (the standard starting point)
- [ ] [Portkey](https://portkey.ai) — managed alternative with built-in guardrails/observability, no ops overhead
- [ ] [AWS Bedrock — Claude models](https://aws.amazon.com/bedrock/anthropic/) — Amazon's managed platform for foundation models (Claude, Llama, Mistral, Titan) inside the AWS security boundary
- [ ] [Anthropic docs — Claude on Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)
- [ ] [Claude Code — Amazon Bedrock setup](https://code.claude.com/docs/en/amazon-bedrock) — relevant since Claude Code can run directly against Bedrock

**POC**
- [ ] Stand up a local LiteLLM proxy routing requests between the Anthropic API and a local Ollama model behind a single OpenAI-compatible endpoint.
- [ ] Run `/setup-bedrock` in Claude Code to authenticate against AWS Bedrock and compare behavior/latency with the direct API.

---

## Phase 3 — MCP (Model Context Protocol)
*(1 week)*

**Reading**
- [X] [Official announcement](https://www.anthropic.com/news/model-context-protocol)
- [X] [Official docs](https://modelcontextprotocol.io) — host/client/server architecture, Tools/Resources/Prompts

**Repos**
- [X] [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — reference MCP servers (filesystem, git, etc.)
- [X] [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) (or `typescript-sdk`, depending on your stack)

**POC**
- [X] Build a simple MCP server (Python or TS) with 1 Tool (e.g., query an internal API) and 1 Resource.
- [X] Connect it to Claude Desktop or Claude Code.

---

## Phase 4 — Claude Skills, Commands & Rules
*(3–5 days)*

Builds directly on the custom subagents you already run in Claude Code (`~/.claude/agents/`) — Skills, Commands, and Rules are the other three ways to shape how Claude Code behaves per-project.

**Reading**
- [ ] [Skills](https://code.claude.com/docs/en/skills) — reusable, on-demand instruction packages Claude loads only when relevant
- [ ] [Slash Commands](https://code.claude.com/docs/en/commands) — reusable prompt templates invoked with `/name`
- [ ] [Memory & Rules (CLAUDE.md, `.claude/rules/`)](https://code.claude.com/docs/en/memory) — persistent, path-scoped project instructions
- [ ] [Sub-agents](https://code.claude.com/docs/en/sub-agents) — for reference against what you've already configured

**POC**
- [ ] Create a custom Skill for a repetitive task in one of your projects (e.g., a code-review checklist or a report-generation format).
- [ ] Write a custom slash command (e.g., `/test-report` or `/deploy-check`).
- [ ] Add path-scoped rules under `.claude/rules/` for a multi-package repo.

---

## Phase 5 — RAG (Retrieval-Augmented Generation)
*(1–2 weeks)*

**Reading**
- [ ] [Original RAG paper (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401)
- [ ] [LangChain — official RAG tutorial](https://docs.langchain.com/oss/python/langchain/rag)

**Repo (most complete)**
- [ ] [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) — from basic RAG to advanced techniques (reranking, chunking, agentic RAG), with ready-to-run LangChain and LlamaIndex notebooks

**POC**
- [ ] Simple RAG: your own PDFs → ChromaDB (local) → embeddings → LLM query.
- [ ] Level up to "reliable RAG" (validating retrieved chunk relevance) using the repo above.

---

## Phase 6 — Running Models Locally
*(1 week)*

**Tools (easiest to most control)**
1. [ ] **Ollama** — simplest, local API on port 11434: [ollama/ollama](https://github.com/ollama/ollama)
2. [ ] **LM Studio** — GUI, good for exploring models: [lmstudio.ai](https://lmstudio.ai)
3. [ ] **llama.cpp** — the engine under Ollama/LM Studio, full control over flags/quantization: [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

**Reading**
- [ ] Quantization basics (Q4/Q5/Q6/Q8) and the GGUF format — any 2026 Ollama vs. llama.cpp guide covers this quickly.

**POC**
- [ ] `ollama pull llama3.2` + `ollama run llama3.2` → test locally.
- [ ] Swap the Phase 5 RAG backend from a paid API to local Ollama (embeddings + generation fully local).

---

## Phase 7 — Multi-Agent Systems
*(1–2 weeks)*

Single agents hit a ceiling on complex, multi-step work. Multi-agent systems split the work across specialized agents that plan, delegate, and review each other.

**Reading**
- [ ] [LangGraph docs](https://langchain-ai.github.io/langgraph/) — graph-based orchestration, most control, steepest learning curve
- [ ] [CrewAI docs](https://docs.crewai.com) — role-based crews (Agent/Task/Crew), easiest to start with
- [ ] [Microsoft AutoGen](https://github.com/microsoft/autogen) — conversational, agent-vs-agent design
- [ ] [Claude Code — Agent Teams](https://code.claude.com/docs/en/agent-teams) — built-in multi-agent orchestration, a natural extension of the subagents you already use

**POC**
- [ ] Build a small research crew (CrewAI or LangGraph): one agent researches, one writes, one reviews.
- [ ] Try Claude Code's native Agent Teams feature on a real task and compare it to your existing subagent setup.

---

## Phase 8 — Agent Evaluation & Benchmarks
*(1 week)*

Building an agent is easy; knowing whether it's actually good is not. This phase is about measuring behavior, not just shipping it.

**Reading**
- [ ] [Anthropic Engineering — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — how to structure evals for multi-turn, tool-using agents
- [ ] [SWE-bench](https://www.swebench.com) — real-world coding-agent benchmark (GitHub issues → verified patches)
- [ ] [GAIA benchmark](https://huggingface.co/datasets/gaia-benchmark/GAIA) — general-assistant tasks requiring tools, browsing, multi-step reasoning
- [ ] [tau-bench](https://github.com/sierra-research/tau-bench) — tool-agent-user benchmark, tests policy adherence in realistic conversations

**POC**
- [ ] Write a small private eval (10–20 tasks) for one of your own agents/POCs from earlier phases: define inputs, expected outcomes, and a grading function.
- [ ] Run that eval against two different models or two different prompt/tool configurations and compare pass rates.

---

## Phase 9 — Capstone Project
*(1–2 weeks)*

Combine everything: **local model + RAG + multi-agent orchestration, exposed as an MCP server**, plugged into Claude Code/Desktop, with a basic eval suite to check it's actually working.

Example: an MCP server exposing a `search_knowledge_base` Tool → backed by local RAG (Ollama + ChromaDB) over your own documents, orchestrated by a small agent team (research → answer → review), routed through a local AI gateway, with a handful of eval cases guarding against regressions. A fully private/offline assistant accessible from inside Claude Code.

---

## Priority Order (Short on Time)

`MCP (Phase 3)` → `RAG (Phase 5)` → `Local (Phase 6)` → `Multi-Agent (Phase 7)` → `Integration (Phase 9)`

Fundamentals (Phase 0), Gateways/Bedrock (Phase 2), Claude Skills/Commands/Rules (Phase 4), and Evaluation (Phase 8) can run in parallel, in spare time.

## License

MIT
