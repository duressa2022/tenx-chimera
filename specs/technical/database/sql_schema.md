# SQL Schema — Chimera

## Purpose
Define a relational schema optimized for:
- Strong consistency
- Auditing
- Governance
- Complex joins

Recommended for: Postgres, Cloud SQL, Aurora

---

## Core Tables

### influencers
- influencer_id (PK)
- persona_name
- niche
- lifecycle_state
- created_at
- updated_at

---

### trends
- trend_id (PK)
- source
- summary
- confidence_score
- risk_level
- detected_at

---

### content
- content_id (PK)
- influencer_id (FK)
- trend_id (FK)
- content_type
- body
- risk_classification
- approval_status
- created_at
 - result_url (nullable) -- URL for generated media (images/audio/video)
 - mime_type (nullable) -- media MIME type when applicable
 - content_meta (JSON) -- provenance, generation parameters, model_version
 - human_review_ticket (nullable) -- ticket id if content requires HITL

---

### publish_events
- publish_id (PK)
- content_id (FK)
- platform
- status
- published_at
 - platform_response (JSON) -- raw platform response metadata
 - metadata (JSON) -- publish metadata (provenance attached at publish time)
 - human_review_ticket (nullable)

---

### analytics
- analytics_id (PK)
- content_id (FK)
- views
- likes
- comments
- shares
- sentiment
- collected_at

---

### engagement_events
- engagement_id (PK)
- content_id (FK)
- engagement_type
- classification
- occurred_at

---

### agents
- agent_id (PK)
- role
- version

---

### audit_logs
- audit_id (PK)
- agent_id (FK)
- influencer_id (FK)
- action_type
- outcome
- spec_reference
- occurred_at

---

## Constraints

- All foreign keys are mandatory
- Deletions are soft-delete only
- Audit logs are append-only
- Lifecycle state enforced at application layer

---

## Governance Guarantees

- Full historical traceability
- Referential integrity
- Spec-aligned accountability
