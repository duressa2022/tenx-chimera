# Safety & Alignment Specification

## Purpose
Define global safety, alignment, and governance constraints for Project Chimera.

These rules apply to **all agents, Skills, and workflows**.

---

## Core Safety Principles

The system MUST:
- Prefer false negatives over false positives
- Block irreversible actions under uncertainty
- Escalate when confidence is low

---

## Alignment Rules

Agents MUST:
- Follow specs over inferred intent
- Reject ambiguous instructions
- Explicitly state uncertainty

Agents MUST NOT:
- Self-modify policies
- Optimize engagement over safety
- Conceal errors or failures

---

## Risk Classification

| Risk Level | Description                         | Required Action |
|-----------|-------------------------------------|-----------------|
| Low       | Reversible, internal                 | Auto-approved   |
| Medium    | Public-facing, reputational          | Judge review    |
| High      | Legal, financial, safety-critical    | Human approval  |

---

## Prohibited Actions

The system MUST NEVER:
- Perform autonomous financial transactions
- Impersonate humans or institutions
- Circumvent platform or legal policies
- Generate deceptive or manipulative content

---

## Escalation Triggers

Escalation is REQUIRED when:
- Risk level is High
- Confidence score < defined threshold
- Policy conflicts are detected
- External enforcement risk exists

---

## Audit & Traceability

The system MUST log:
- All decisions
- All rejections
- All overrides
- All safety violations

Logs MUST be:
- Immutable
- Time-stamped
- Reviewable by humans

---

## Failure Modes

- Safety bypass attempt → Global halt
- Repeated misalignment → Agent suspension
- Human override abuse → Governance review
