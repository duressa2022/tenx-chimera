
---

# `inter_agent_messaging.md`

```md
# OpenClaw Inter-Agent Messaging Specification

## Purpose
Define safe, structured communication between Chimera Agents and other OpenClaw agents.

---

## Messaging Principles

All inter-agent communication MUST be:
- Explicit
- Structured
- Logged
- Authenticated

---

## Message Types

- Capability Discovery
- Task Offer
- Task Acceptance
- Task Rejection
- Status Update
- Safety Escalation

---

## Message Envelope Schema

```json
{
  "message_id": "uuid",
  "sender_agent_id": "string",
  "receiver_agent_id": "string",
  "message_type": "string",
  "payload": {},
  "timestamp": "ISO-8601 timestamp",
  "signature": "string"
}
