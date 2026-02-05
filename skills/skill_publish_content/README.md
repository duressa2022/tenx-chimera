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
- Orchestrator

Planner Agents are explicitly forbidden.

---

## Preconditions (Hard)

ALL must be true before execution:

- Influencer lifecycle state == `Active`
- Content approval_status == `approved`
- Content risk_classification != `high`
- Platform connector available via MCP
- Input contract validates

If any precondition fails → immediate hard failure.

---

## Postconditions

On success:
- Content is published to exactly one platform
- Platform response metadata is returned
- Publish event is emitted

On failure:
- No retries unless error is classified as transient
- Failure event is emitted

---

## Irreversibility Notice

Once a publish request is accepted by a platform:
- The action CANNOT be undone by Chimera
- Rollback is NOT guaranteed
- Human intervention may be required
