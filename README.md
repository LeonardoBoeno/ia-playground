# AI Learning Roadmap: MCP, RAG & Local LLMs

> A sequential, hands-on study path to understand modern AI systems — from LLM fundamentals to Model Context Protocol (MCP), Retrieval-Augmented Generation (RAG), and running your own models locally.

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)

## About

This repo tracks my personal learning path through core AI engineering topics. Each phase includes curated readings, videos, reference repos, and a hands-on POC to validate the concept before moving on.

**Estimated time:** 6–8 weeks (part-time)

## Table of Contents

- [Phase 0 — AI/LLM Fundamentals](#phase-0--aillm-fundamentals)
- [Phase 1 — APIs & Prompt Engineering](#phase-1--apis--prompt-engineering)
- [Phase 2 — MCP (Model Context Protocol)](#phase-2--mcp-model-context-protocol)
- [Phase 3 — RAG (Retrieval-Augmented Generation)](#phase-3--rag-retrieval-augmented-generation)
- [Phase 4 — Running Models Locally](#phase-4--running-models-locally)
- [Phase 5 — Capstone Project](#phase-5--capstone-project)
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
- [ ] [Anthropic — Prompt Engineering Overview](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [ ] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)

**POC**
- [ ] Script calling the Anthropic (or OpenAI) API with basic tool use / function calling — e.g., a small "agent" that queries a weather API.

---

## Phase 2 — MCP (Model Context Protocol)
*(1 week)*

**Reading**
- [ ] [Official announcement](https://www.anthropic.com/news/model-context-protocol)
- [ ] [Official docs](https://modelcontextprotocol.io) — host/client/server architecture, Tools/Resources/Prompts

**Repos**
- [ ] [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — reference MCP servers (filesystem, git, etc.)
- [ ] [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) (or `typescript-sdk`, depending on your stack)

**POC**
- [ ] Build a simple MCP server (Python or TS) with 1 Tool (e.g., query an internal API) and 1 Resource.
- [ ] Connect it to Claude Desktop or Claude Code.

---

## Phase 3 — RAG (Retrieval-Augmented Generation)
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

## Phase 4 — Running Models Locally
*(1 week)*

**Tools (easiest to most control)**
1. [ ] **Ollama** — simplest, local API on port 11434: [ollama/ollama](https://github.com/ollama/ollama)
2. [ ] **LM Studio** — GUI, good for exploring models: [lmstudio.ai](https://lmstudio.ai)
3. [ ] **llama.cpp** — the engine under Ollama/LM Studio, full control over flags/quantization: [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

**Reading**
- [ ] Quantization basics (Q4/Q5/Q6/Q8) and the GGUF format — any 2026 Ollama vs. llama.cpp guide covers this quickly.

**POC**
- [ ] `ollama pull llama3.2` + `ollama run llama3.2` → test locally.
- [ ] Swap the Phase 3 RAG backend from a paid API to local Ollama (embeddings + generation fully local).

---

## Phase 5 — Capstone Project
*(1–2 weeks)*

Combine everything: **local model + RAG, exposed as an MCP server**, plugged into Claude Code/Desktop.

Example: an MCP server exposing a `search_knowledge_base` Tool → backed by local RAG (Ollama + ChromaDB) over your own documents. A fully private/offline assistant accessible from inside Claude Code.

---

## Priority Order (Short on Time)

`MCP (Phase 2)` → `RAG (Phase 3)` → `Local (Phase 4)` → `Integration (Phase 5)`

Fundamentals (Phase 0) can run in parallel, in spare time.

## License

MIT