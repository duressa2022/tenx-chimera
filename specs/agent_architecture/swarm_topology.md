# Agent Architecture Spec: Swarm Topology

## Purpose
Define how agents are connected, scaled, and isolated within the Chimera system.

---

## Topology Model

Chimera SHALL use a **Hub-and-Spoke Swarm Topology**.

- Hub: Orchestrator (Planner + Judge)
- Spokes: Stateless Worker Agents

---

## Communication Rules

- Planner → Worker: Task Contract (JSON)
- Worker → Judge: Result Contract (JSON)
- Worker → Worker communication is PROHIBITED

---

## State Management

| Component | State Policy |
|--------|-------------|
| Planner | Persistent |
| Worker | Stateless |
| Judge | Stateless |

All persistent state MUST live outside agents.

---

## Scaling Rules

- Workers scale horizontally
- Workers are disposable
- Planner and Judge are logically centralized

---

## Failure Isolation

- Worker failure → retry or reassignment
- Judge rejection → task refinement
- Orchestrator failure → replay from event log

---

## Non-Goals

- Peer-to-peer agent collaboration
- Emergent swarm decision making
- Long-lived worker memory
