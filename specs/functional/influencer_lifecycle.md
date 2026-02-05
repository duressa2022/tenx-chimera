# Functional Spec: Influencer Lifecycle

## Purpose
Define how Autonomous Influencers are created, activated, governed,
paused, and retired within Project Chimera.

---

## Actors
- Orchestrator
- Planner Agent
- Human Reviewer

---

## Lifecycle States

An Influencer MUST exist in exactly one of the following states:

1. **Draft**
2. **Approved**
3. **Active**
4. **Suspended**
5. **Retired**

State transitions outside this graph are invalid.

---

## State Definitions

### Draft
- Influencer identity exists
- No external actions permitted
- Skills MAY NOT be executed

### Approved
- Human reviewer has approved influencer configuration
- Ready for activation
- No publishing allowed yet

### Active
- Influencer may:
  - Research trends
  - Generate content
  - Publish content
  - Engage with users
- All actions MUST be logged

### Suspended
- Triggered by:
  - Policy violation
  - Manual human intervention
  - Safety uncertainty
- No outward-facing actions permitted

### Retired
- Permanent shutdown
- Data retained for audit
- No reactivation allowed

---

## Governance Rules

- Transition into **Approved** requires Human-in-the-Loop approval
- Transition into **Active** requires:
  - Valid specs
  - Skills availability
  - Safety policy confirmation
- Any agent may recommend suspension
- Only humans may approve reactivation

---

## Failure Modes

- Undefined state transition → System error
- Missing approval → Hard stop
- Skill execution in invalid state → Violation event
