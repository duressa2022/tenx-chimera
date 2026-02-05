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

---

### Trend Selection
Only trends that meet ALL criteria may proceed:
- Confidence score ≥ threshold
- Policy compliance = true
- No duplication with recent content

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

---

## Failure Modes

- Conflicting data → escalate to Judge
- Insufficient confidence → discard
- Policy ambiguity → HITL required
