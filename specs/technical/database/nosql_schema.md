# NoSQL Schema — Chimera

## Purpose
Define a schema optimized for:
- High write throughput
- Event-heavy systems
- Horizontal scaling

Recommended for: MongoDB, DynamoDB, Firestore

---

## Collections

### influencers
```json
{
  "influencer_id": "string",
  "persona": {
    "name": "string",
    "niche": "string"
  },
  "lifecycle_state": "Active",
  "created_at": "datetime"
}

### trends
{
  "trend_id": "string",
  "source": "string",
  "summary": "string",
  "confidence_score": 0.92,
  "risk_level": "low",
  "detected_at": "datetime"
}

### content
{
  "content_id": "string",
  "influencer_id": "string",
  "trend_id": "string",
  "type": "script",
  "body": "string",
  "risk_classification": "medium",
  "approval_status": "approved",
  "created_at": "datetime"
}

### events (polymorphic)
{
  "event_id": "string",
  "event_type": "publish | engagement | analytics | audit",
  "entity_id": "string",
  "payload": {},
  "occurred_at": "datetime"
}
