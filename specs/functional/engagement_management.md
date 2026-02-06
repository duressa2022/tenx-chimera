# Functional Spec: Engagement Management

## Purpose
Define how agents respond to audience interactions.

---

## Actors
- Engagement Agent
- Judge Agent
- Human Reviewer

---

## Engagement Types
- Comments
- Mentions
- Direct messages
- Media replies (image, audio, video attachments)

---

## Functional Requirements

### Classification
Incoming engagement MUST be classified as:
- Benign
- Question
- Criticism
- Harassment
- Sensitive
- Impersonation / Voice-clone
- Copyright claim

---

### Response Rules

- Benign → auto-response allowed
- Question → factual response only
- Criticism → neutral tone required
- Sensitive → HITL mandatory
- Harassment → ignore or escalate
- Impersonation / voice-clone indicators → escalate to HITL and do NOT generate an imitation reply

Media-specific rules:

- If an incoming engagement includes media (image/audio/video), extract and attach provenance metadata and run media moderation checks before responding.
- Do not accept or reproduce media that appears to violate privacy, contains minors, or is pornographic.

---

## Governance Constraints

- No emotional manipulation
- Personal data handling requires explicit authorization and must be avoided by default
- All responses MUST be logged with provenance and `format_options` used to generate any media responses
- Any automated media generation for a reply that includes impersonation indicators is forbidden without explicit human approval

---

## Failure Modes

- Misclassification → Judge correction
- Escalation ignored → violation
