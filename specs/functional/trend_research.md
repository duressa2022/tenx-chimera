# Functional Spec: Trend Research

## Purpose
Define how agents discover, evaluate, and select trends
for content generation.

---

## Actors
- Planner Agent
- Worker Agent
- External Trend Data Sources (via MCP)

---

## Functional Requirements

### Trend Discovery
The system MUST:
- Query multiple trend sources
- Normalize trend data into a common structure
- Assign confidence scores

---

### Trend Evaluation
Each trend MUST be evaluated for:
- Relevance to influencer niche
- Recency
- Engagement potential
- Safety and policy compliance

Additional media-aware evaluation:

- Assess whether recommended content formats are text, image, audio, or video and include `recommended_content_types` in the output.
- Check example media samples for licensing and provenance; flag samples that include third-party copyrighted material.
- Detect signs of manipulated media (deepfakes, doctored images, voice cloning) and escalate to human review if detected.

---

### Trend Selection
Only trends that meet ALL criteria may proceed:
- Confidence score ≥ threshold
- Policy compliance = true
- No duplication with recent content

If a trend is flagged as high risk during evaluation (privacy, copyright, deepfake potential), the skill MUST create a `human_review_ticket` and withhold publishable media examples until review completes.

---

## Governance Constraints

- Agents MUST explain why a trend was selected
- Human review MAY be required for sensitive domains
- Unsafe trends MUST be discarded automatically

---

## Outputs

A validated trend object MUST include:
- Source
- Timestamp
- Summary
- Risk classification
- Selection rationale

Optional / recommended outputs:
- `recommended_content_types`: ordered list of suggested media formats (e.g., ["video","short_text"]).
- `example_media`: list of example media samples (URL, mime_type) that illustrate the trend.
- `provenance`: object describing sources and retrieval parameters.
- `human_review_ticket`: present when trend requires manual review.

---

## Failure Modes

- Conflicting data → escalate to Judge
- Insufficient confidence → discard
- Policy ambiguity → HITL required
