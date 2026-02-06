# Functional Spec: Content Generation

## Purpose
Define how validated trends are transformed into publishable content.

---

## Actors
- Planner Agent
- Content Worker Agent
- Judge Agent
- Human Reviewer (optional)

---

## Content Types
- Text posts
- Short-form video scripts
- Captions
- Hashtags
- Images (rendered/AI-assisted)
- Audio (TTS / short clips)
- Video (short-form clips)

---

## Functional Requirements

### Generation
The system MUST:
- Use only approved trends
- Generate content aligned with influencer persona
- Respect tone and platform constraints
- Support producing content in the requested media type (`text`, `image`, `audio`, `video`) and accept `format_options` (e.g., image resolution, audio voice, video aspect ratio)

---

### Validation
Generated content MUST be checked for:
- Policy compliance
- Factual consistency
- Tone alignment
- Harmful or misleading content
- Media-specific checks (image/video deepfake detection, voice-clone detection, identifiable-person likeness)
- Provenance and licensing: ensure provenance metadata is attached and copyrighted material is not reproduced verbatim without license or attribution

---

### Media-Specific Requirements

#### Character Consistency Lock (FR 3.1)
The system SHALL enforce visual identity across all generated media:
- **Identifier:** Every generation task MUST inject the `visual_consistency_id` from `SOUL.md` into the tool payload.
- **Reference:** Workers MUST provide the canonical style LoRA or reference image to the generation MCP server (e.g., Ideogram, Midjourney).
- **Validation:** The Judge agent MUST use a Vision model to verify facial/style resemblance before approval.

#### Hybrid Video Rendering Strategy (FR 3.2)
To optimize for both quality and cost, the system SHALL implement a tiered rendering strategy:
- **Tier 1 (Episodic):** Standard Image-to-Video (Living Portraits) for daily engagement.
- **Tier 2 (Hero):** Full Text-to-Video (Runway/Sora) for primary campaign milestones.
- **Selection:** The Planner MUST determine the tier based on `priority` and `campaign_budget`.

---

## Approval Flow
- Low-risk content → auto-approved
- Medium-risk → Judge review
- High-risk → Human-in-the-Loop required (no auto-publish)

Notes:
- The skill output MUST include `risk_classification` and `provenance` metadata.
- If `risk_classification == high`, the system MUST create a `human_review_ticket` and block publishing until approved.

---

## Governance Constraints

- No content may bypass validation
- Rejected content MUST include rationale
- Approved content MUST be traceable to a trend and include provenance metadata (`trend_id`, `model_version`, `generated_at`, `source_sample_urls` where applicable)
- Media outputs MUST include `mime_type` and, for media served via URLs, a `metadata` object describing generation parameters and any third-party services used

---

## Failure Modes

- Hallucinated facts → rejection
- Policy conflict → suspension recommendation
- Repeated failure → influencer suspension
