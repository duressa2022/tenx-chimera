# Skill: Trend Fetch

## Skill ID
skill_trend_fetch

## Purpose
Fetch, normalize, and score trends from external sources via MCP.

This skill ONLY collects data.
It does NOT select trends.
It does NOT make decisions.

---

## Allowed Callers
- Planner Agent
- Worker Agent

---

## Preconditions

- Influencer lifecycle state MUST be Active
- MCP trend source MUST be reachable
- Input schema MUST validate

---

## Postconditions

- A normalized trend object is returned
- Confidence score is computed
- Risk level is assigned
- Event is emitted

---

## Forbidden Behavior

- Filtering trends based on preference
- Inferring intent
- Writing to storage
