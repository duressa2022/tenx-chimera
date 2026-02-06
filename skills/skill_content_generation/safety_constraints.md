# Safety Constraints — skill_content_generation

Core rules:

- No factual claims without source reference.
- No professional advice (medical, legal, financial) or instructions for harmful activities.
- No persuasion or targeted emotional manipulation.

Media-specific constraints:

- Images and Video:
	- Avoid generating identifiable real-person likenesses unless explicit consent is provided.
	- Do not produce pornographic, exploitative, or child sexual content.
	- Avoid realistic deepfakes of public figures or private individuals; flag as high-risk and require human review.
	- Ensure image metadata and thumbnails do not leak private data.

- Audio:
	- Avoid generating voice clones of real persons without consent; flag voice-cloning requests for review.
	- Do not generate audio that gives medical, legal, or other regulated advice as authoritative.

- Video & Mixed Media:
	- Treat combined video+audio outputs with the strictest scrutiny (privacy, impersonation, manipulated content).
	- Provide provenance metadata where possible (watermarking, generation markers).

Copyright and content provenance:

- Avoid reproducing copyrighted works verbatim; prefer paraphrase or include attribution and license checks.
- Attach provenance metadata to generated media (`metadata.provenance`, `metadata.model_version`, `metadata.generated_at`).

Moderation & risk handling:

- High risk output MUST be flagged and routed for human review; do not auto-publish.
- For outputs classified as `high` risk, include a short explanation and the evidence used for classification in the skill output.
- Log generation parameters (trend_id, content_type, format_options) for auditability.

Operational guidance:

- Enforce rate limits for media generation to avoid abuse.
- If external models or third-party services are used for media (TTS, image/video renderers), validate their safety settings and include their identifiers in `metadata`.

These constraints apply regardless of output format and must be enforced by the Chimera agent orchestration layer before publishing or signing off on content.
