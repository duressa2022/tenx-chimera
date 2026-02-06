# Skill: Publish Content

## Skill ID
skill_publish_content

## Purpose
Publish previously approved content to external platforms via MCP.

This skill performs **irreversible external actions**.
It MUST be tightly governed.

---

## Scope

This skill:
- Publishes approved content
- Supports multiple content types
- Interfaces ONLY through MCP

This skill does NOT:
- Generate content
- Modify content
- Approve content
- Retry unsafe failures

---

## Allowed Callers

- Worker Agent

Planner Agents are explicitly forbidden.

---

## Preconditions (Hard)

ALL must be true before execution:

 - Content `content_meta.risk_classification` != `high` (high-risk content must be human-reviewed before publish)
 - Provenance metadata attached in `content_meta.provenance`

If any precondition fails → immediate hard failure.


## Postconditions

On success:

On failure:
 - If publish is blocked due to `high` risk, a `human_review_ticket` is created and returned in the response

---

## Irreversibility Notice

Once a publish request is accepted by a platform:
- The action CANNOT be undone by Chimera
- Rollback is NOT guaranteed
- Human intervention may be required
