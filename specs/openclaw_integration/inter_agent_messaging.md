
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
  "nonce": "string (for replay protection)",
  "expiry": "ISO-8601 timestamp (optional)",
  "idempotency_key": "string (optional)",
  "signature": "string",
  "signature_algorithm": "string (e.g., RS256)",
  "error_code": "string (optional)"
}


Notes:
- Messages MUST include a `nonce` or sequence number and may include `expiry` to limit replay windows.
- Signatures MUST use a canonical serialization defined by the integration (e.g., JSON Canonicalization Scheme) and the `signature_algorithm` claim.
- Receivers SHOULD validate `idempotency_key` for idempotent operations and return structured `error_code` values for retry logic.
