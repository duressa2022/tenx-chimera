# Tooling Strategy: The Chimera Tech Stack

## Vision
To utilize the "Best-of-breed" tools identified in the a16z Trillion Dollar Stack to ensure Chimera is production-ready and highly observable.

## 1. Core Developer Stack
- **IDE:** Cursor / VS Code (utilizing project-specific `.cursor/rules`).
- **Dependency Management:** `uv` (for ultra-fast, frozen environments).
- **Communication Protocol:** Model Context Protocol (MCP) as the universal interface for all external tools.

## 2. Infrastructure & Operations
- **Dependency Isolation:** Docker multi-stage builds (verified in our root `Dockerfile`).
- **Task Scheduling:** `make` + GitHub Actions (CI/CD pipeline).
- **Environment Management:** Local `.venv` synced via `uv`.

## 3. Specialized AI Tools
- **Vector Database:** Weaviate (Optimized for RAG and hybrid searches).
- **Economic Agency:** Coinbase AgentKit (CdpEvmWalletProvider).
- **Sandboxes:** E2B / Runloop (for safe agentic code execution during the "Code" phase of the loop).
- **Search:** Tavily / Exa (for "long-tail" knowledge retrieval outside the primary trend database).

## 4. Monitoring & Provenance
- **Telemetry:** Tenx MCP Sense (Primary audit trail).
- **Version Control:** Integration-first approach, treating Git as a backend ledger for intent-based commits.
- **Testing:** Pytest-driven TDD (verifying "Red" baselines as implemented in `tests/tdd_srs/`).
