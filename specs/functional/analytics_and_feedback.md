# Functional Spec: Analytics & Feedback

## Purpose
Define how Chimera learns without self-modifying intent.

---

## Actors
- Analytics Agent
- Planner Agent
- Human Reviewer

---

## Metrics Tracked
- Engagement rates
- Reach
- Sentiment
- Content performance

---

## Functional Requirements

- Collect metrics passively
- Store metrics immutably
- Generate insights, not decisions

---

## Feedback Usage

Agents MAY:
- Adjust scheduling
- Recommend content direction

Agents MAY NOT:
- Modify goals
- Modify specifications
- Override governance rules

---

## Governance Constraints

- Insights are advisory only
- Changes require approval
- Drift detection required

---

## Failure Modes

- Metric anomaly → investigation
- Feedback loop detected → halt
