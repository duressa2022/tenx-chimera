# Chimera Skills Registry

## Purpose

This directory defines all **runtime skills** available to Chimera agents.

A Skill is:
- A bounded capability
- Invoked explicitly by agents
- Governed by strict input/output contracts
- Auditable and testable

If a capability is not defined here, **agents cannot use it**.

---

## Skill Rules (Hard Constraints)

- Skills are NOT intelligent
- Skills do NOT decide
- Skills do NOT chain other skills
- Skills MUST validate inputs before execution
- Skills MUST return structured outputs or structured failures

Agents MAY call skills.
Skills MAY NOT call agents.

---

## Skill Lifecycle

1. Input validation
2. Precondition checks
3. Execution
4. Output validation
5. Event emission

Failure at any stage MUST short-circuit execution.

---

## Registered Skills

- skill_trend_fetch
- skill_content_generation
- skill_publish_video
- skill_engagement_manager
