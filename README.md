# Project Chimera

Project Chimera is a **spec-driven agentic infrastructure** for building,
governing, and operating Autonomous AI Influencers.

This repository is intentionally **spec-first**.
Implementation exists to satisfy specifications — never the other way around.

---

## What This Repository Is

- A **factory** for autonomous agents
- A **governed environment** for AI contribution
- A **source of truth** for agent behavior, safety, and constraints
- A **testable contract** between humans, agents, and infrastructure

---
# Project Chimera: The Autonomous Influencer Factory

Project Chimera is a professional-grade agentic infrastructure designed to build and govern the "Autonomous Influencer"—a digital entity capable of trend research, content generation, and autonomous engagement.

## 🚀 Vision
Built on the principles of **Spec-Driven Development (SDD)** and **Optimistic Concurrency Control (OCC)**, Chimera ensures that AI agents operate within strict safety guardrails and verifiable execution paths.

## 🏗️ Architecture
- **Agent Pattern:** Hierarchical Swarm (Planner-Worker-Judge)
- **Engine:** Python 3.12 + `uv`
- **Infrastructure:** Dockerized with CI/CD Governance
- **State Management:** Optimistic Concurrency for the Agent Social Network

## 📁 Repository Structure
- `specs/`: Single source of truth. Contains functional, technical, and openclaw specifications.
- `skills/`: Runtime capabilities available to agents (with strict I/O contracts).
- `tests/`: TDD-based suite. Failing tests define the implementation "slots" for agents.
- `research/`: Domain mastery and agent social protocol analysis.
- `scripts/`: Verification and spec-compliance tools.
- `.github/`: CI/CD and governance automation
- `.cursor/`: IDE agent rules
- `Dockerfile`: Reproducible execution environment
- `Makefile`: Standardized commands

## 🛠️ Quick Start

### Prerequisites
- Docker
- Python 3.12+
- `uv` (recommended)

### Local Setup
```bash
make setup
```

### Run Verification (Failing Tests)
```bash
make test
```

### Check Spec Alignment
```bash
make spec-check
```

## 🛡️ Governance
All agent activity is governed by the **Prime Directive** defined in `.cursor/rules`. Each change must be:
1. Ratified by a specification.
2. Verified by a test.
3. Reviewed by an AI Governor (`.coderabbit.yaml`).

## 🖇️ OpenClaw Integration
Chimera integrates with the OpenClaw Agent Social Network using standards defined in `specs/openclaw_integration/`.
