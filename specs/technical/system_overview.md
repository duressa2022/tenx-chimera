# System Overview — Project Chimera

## Purpose

This document defines the high-level technical architecture of Project Chimera,
describing how agents, skills, MCP servers, APIs, and governance layers interact.

This is a **descriptive system contract**, not an implementation guide.

---

## System Composition

Project Chimera consists of six primary layers:

1. Agent Runtime
2. Orchestration & Governance
3. Skills Layer
4. MCP Integration Layer
5. Data & Persistence
6. Observability & Audit

---

## 1. Agent Runtime

The Agent Runtime hosts all autonomous agents and enforces:

- Role separation (Planner, Worker, Judge)
- Lifecycle state constraints
- Skill invocation rules
- Context isolation between agents

Agents MAY NOT:
- Access external systems directly
- Modify their own specifications
- Persist data outside defined schemas

---

## 2. Orchestration & Governance Layer

The Orchestrator is the authoritative control plane.

Responsibilities:
- Agent lifecycle management
- Task routing and scheduling
- Human-in-the-Loop enforcement
- Policy and safety escalation

All irreversible actions MUST pass through this layer.

---

## 3. Skills Layer

Skills are first-class, versioned capability packages.

Characteristics:
- Strict input/output contracts
- Deterministic behavior where possible
- No hidden side effects
- Explicit failure modes

Agents MAY ONLY act through skills.

---

## 4. MCP Integration Layer

All external interactions occur via MCP servers.

This includes:
- Trend data providers
- Social media platforms
- Databases
- File systems

Direct API calls are prohibited.

---

## 5. Data & Persistence

Data is divided into:
- Operational data (content, trends)
- Analytics data (metrics)
- Governance data (logs, decisions)

All writes MUST be auditable.
All schemas MUST be versioned.

---

## 6. Observability & Audit

The system MUST provide:
- Immutable audit logs
- Agent decision traces
- Skill invocation history
- Governance events

Tenx MCP Sense acts as the primary telemetry recorder.

---

## Non-Negotiable Guarantees

- Every action is attributable
- Every output is traceable
- Every failure is observable
- Every decision is interruptible
