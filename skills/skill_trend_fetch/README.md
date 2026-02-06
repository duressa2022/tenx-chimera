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

Additional outputs and notes:

- The returned trend object may include `recommended_content_types` (text, image, video, audio) and `example_media` samples.
- The skill will attach `provenance` metadata describing sources and retrieval parameters.
- If a trend is classified as `high` risk (privacy, copyright, deepfake potential), the skill will create a `human_review_ticket` and not surface publishable examples until review.

---

## Forbidden Behavior

- Filtering trends based on preference
- Inferring intent
- Writing to storage
