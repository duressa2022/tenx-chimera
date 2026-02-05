# Event Models — Project Chimera

## Purpose

This document defines the canonical event model used throughout Project Chimera.
Events are the **single source of truth** for what happened, why it happened,
and which specification authorized it.

State is derived from events.
Agents do not mutate state directly.

---

## Design Principles

- Events are immutable
- Events are append-only
- Events are auditable
- Events are spec-referenced
- Events are machine-parseable

If an action did not emit an event, it is considered **non-existent**.

---

## Event Taxonomy

All events fall into exactly one category:

1. **Operational Events**
2. **Governance Events**
3. **Analytics Events**
4. **Error Events**

Mixing categories is prohibited.

---

## Base Event Contract

Every event MUST conform to the following structure:

```json
{
  "event_id": "string",
  "event_type": "string",
  "event_category": "operational | governance | analytics | error",
  "source_agent_id": "string",
  "source_agent_role": "planner | worker | judge | orchestrator",
  "influencer_id": "string",
  "spec_reference": "string",
  "payload": {},
  "occurred_at": "ISO-8601 datetime"
}
