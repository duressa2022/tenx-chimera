
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
  "public_key": "string"
}
