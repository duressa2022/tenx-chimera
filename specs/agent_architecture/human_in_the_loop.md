
---

## 📄 `human_in_the_loop.md`

```md
# Agent Architecture Spec: Human-in-the-Loop (HITL)

## Purpose
Define when and how human oversight intervenes in autonomous workflows.

---

## Mandatory HITL Triggers

Human review is REQUIRED when:
- Confidence score < threshold
- Content touches sensitive domains
- Platform policy boundaries are unclear
- Reputation risk is detected

---

## Approval Flow

- Low risk → auto-approved
- Medium risk → Judge approval
- High risk → Human approval required

---

## Human Actions

Humans MAY:
- Approve
- Reject
- Edit
- Suspend agent execution

---

## Kill Switch

A global kill switch MUST exist to:
- Halt all agent execution
- Block publishing
- Freeze financial actions

---

## Governance Constraints

- No autonomous override of human rejection
- All human actions MUST be logged
- Escalation MUST block downstream actions

---

## Failure Modes

- Delayed response → task timeout
- Human override conflict → system pause
- Repeated escalations → agent suspension
