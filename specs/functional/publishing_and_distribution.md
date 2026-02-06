# Functional Spec: Publishing & Distribution

## Purpose
Define how approved content is published across platforms.

---

## Actors
- Publishing Agent
- MCP Platform Connectors
- Human Reviewer (optional)

---

## Functional Requirements

### Pre-Publish Checks
Before publishing:
- Influencer MUST be Active
- Content MUST be approved
- Platform availability confirmed

Additional pre-publish checks for media:

- `content_meta.risk_classification` MUST NOT be `high` (high-risk content requires human review and explicit approval before publish)
- `content_meta.provenance` MUST be present and include source references and `model_version` used to generate media
- License checks MUST pass for any third-party media or assets

---

### Publishing
The system MUST:
- Publish content via MCP only
- Capture platform response metadata
- Retry failed publishes safely

When publishing media:

- Include provenance metadata in the publish payload where supported (watermarking, description fields, or metadata APIs)
- Respect `format_options` (e.g., resolution, aspect ratio) and convert media if necessary before publish
- If a human-review ticket exists, do not publish until status is `approved`

---

## Distribution Rules

- Platform-specific constraints must be respected
- Rate limits must be enforced
- Duplicate content across platforms must be intentional

---

## Governance Constraints

- No direct API access allowed
- Publishing failures MUST be logged
- Policy violations trigger suspension

- Publishing of high-risk content is blocked until human review completes with explicit `approved` state
- Where possible, include generation provenance and a visible indicator on published media to signal it was AI-generated

---

## Failure Modes

- Platform rejection → retry or escalate
- Credential failure → hard stop
- Unexpected response → Judge review
