# Agent Architecture Spec: Agent Patterns

## Purpose
Define the canonical agent pattern used across Project Chimera to ensure scalability, safety, and deterministic behavior.

---

## Actors
- Planner Agent
- Worker Agent
- Judge Agent
- Human Governor (optional)

---

## Selected Pattern

### Hierarchical Swarm (Planner–Worker–Judge)

The system SHALL use a hierarchical swarm architecture where responsibilities are explicitly separated and enforced.

---

## Role Definitions

### Planner Agent
Responsible for:
- Translating specifications into task graphs
- Selecting appropriate Skills
- Defining success and failure criteria

The Planner MUST NOT:
- Execute tools
- Generate final content
- Bypass specs

---

### Worker Agent
Responsible for:
- Executing a single task using an assigned Skill
- Producing structured outputs

The Worker MUST:
- Operate within a bounded context
- Use only registered Skills
- Return outputs matching declared contracts

---

### Judge Agent
Responsible for:
- Validating Worker outputs
- Enforcing safety and governance rules
- Triggering escalation when required

The Judge has final authority over task outcomes.

---

## Governance Constraints

- No Worker may act without a Planner-issued task
- No output may bypass the Judge
- Humans may override any decision

---

## Failure Modes

- Pattern violation → immediate task termination
- Role leakage → system fault
- Unauthorized autonomy → global halt
