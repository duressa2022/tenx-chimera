
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
