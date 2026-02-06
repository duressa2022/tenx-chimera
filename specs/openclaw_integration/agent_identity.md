
---

# `agent_identity.md`

```md
# OpenClaw Agent Identity Specification

## Purpose
Define how Chimera Agents establish a verifiable, non-human identity within the OpenClaw network.

---

## Identity Principles

Agent identity MUST be:
- Persistent
- Verifiable
- Non-human
- Non-transferable

---

## Agent Identity Attributes

```json
{
  "agent_id": "string",
  "agent_name": "chimera_<instance>",
  "agent_type": "autonomous_influencer",
  "owner": "organization | human",
  "governance_model": "human_in_loop",
  "created_at": "ISO-8601 timestamp",
  "public_key": "string",
  "issuer": "string (identity provider or CA)",
  "key_rotation_policy": { "rotation_interval_days": 90, "last_rotated": "ISO-8601 timestamp" },
  "revocation_endpoint": "string (URL to check revocation status)",
  "verifier": { "type": "string", "contact": "string" }
}


Guidance:
- Identity tokens or certificates MUST include `agent_id` and `issuer` claims. Key rotation and revocation processes MUST be documented and auditable.
