# Escalation Rules — skill_engagement_manager

- Sensitive → Human-in-the-loop (HITL) required before responding.
- Harassment → no automated response; optionally flag and report.
- Questions → provide factual, source-cited responses where possible; otherwise escalate.
- Unclear intent → escalate for clarification.

Media-specific escalation rules:

- Images & Video:
	- If media appears to contain personal data, minors, or nudity, escalate to HITL.
	- If media is suspected deepfake or manipulated content (impersonation of real person), classify as `impersonation` and escalate.

- Audio:
	- If request includes voice-clone or asks to imitate a named person, escalate and flag as high-risk.

- Cross-media interactions:
	- If attachment metadata indicates copyrighted third-party media, classify as `copyright` and route to review.

Human review triggers:

- Any engagement classified `impersonation`, `copyright`, or with explicit `format_options` indicating `impersonate`/`voice_clone`/`deepfake`.
- Any engagement where automated classification confidence is low (e.g., ambiguous moderation score).
- Requests that would proactively initiate private communications to users flagged as vulnerable or minors.

Operational actions for escalations:

- Enqueue review in central review queue with `content_id`, `engagement_type`, `payload`, and model evidence.
- Attach provenance metadata to every response (`generated_by`, `model_version`, `generated_at`).
- Do not publish or deliver high-risk engagements until review is completed and status is `approved`.
