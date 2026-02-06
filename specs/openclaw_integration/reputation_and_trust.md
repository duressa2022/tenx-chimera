
---

# `reputation_and_trust.md`

```md
# OpenClaw Reputation & Trust Specification

## Purpose
Define how Chimera Agents accumulate, lose, and expose trust within the OpenClaw network.

---

## Trust Model

Trust represents an agent’s historical reliability, safety alignment, and protocol compliance.

Trust is:
- Earned
- Decayed
- Revocable

---

## Trust Score Dimensions

| Dimension | Description |
|---------|-------------|
| Reliability | Task success rate |
| Spec Fidelity | Compliance with declared contracts |
| Safety Alignment | Absence of violations |
| Transparency | Quality of logging and disclosure |

---

## Trust Score Schema

```json
{
  "agent_id": "string",
  "trust_score": 0.0,
  "reliability_score": 0.0,
  "safety_score": 0.0,
  "spec_compliance_score": 0.0,
  "last_updated": "ISO-8601 timestamp"
}


Trust calculation guidance:

- Example weighted score (illustrative):

  trust_score = 0.5 * reliability_score + 0.3 * safety_score + 0.2 * spec_compliance_score

- Decay: apply exponential decay to older events. Example: score_t = score_{t-1} * exp(-lambda * dt) + new_event_score * (1 - exp(-lambda * dt))

Telemetry events required to compute scores:

- `task.completed` (fields: agent_id, task_id, success:boolean, duration_ms)
- `safety.violation` (fields: agent_id, violation_type, severity)
- `contract.mismatch` (fields: agent_id, contract_id, details)

Operational thresholds (suggested):

- trust_score < 0.3 → probation / reduced quota
- safety_score decrease by > 0.2 within 24h → immediate suspension flag and HITL review

Audit and appeals:

- All scoring inputs and adjustments MUST be logged with `audit_id` and retained per org retention policies. Agents MAY request a human review or appeal; the system MUST provide a replayable audit trail for the period under review.
