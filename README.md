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

## What This Repository Is NOT

- A demo or prototype
- A prompt collection
- A free-form experimentation sandbox
- A content-generation tool

---

## Repository Structure (Authoritative)

```text
specs/        # System intent (source of truth)
skills/       # Agent-executable capabilities (contracts only)
tests/        # Failing tests define expected behavior
.github/      # CI/CD and governance automation
.cursor/      # IDE agent rules
Dockerfile    # Reproducible execution environment
Makefile      # Standardized commands
