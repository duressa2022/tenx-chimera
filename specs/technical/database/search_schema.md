# Search Schema — Elasticsearch

## Purpose
Define mappings for **Elasticsearch** to enable powerful content discovery, full-text search, and faceted reporting.

---

## Indices

### content_discovery
Primary index for exploring published and upcoming content.
- **Mappings:**
    - `content_id`: keyword
    - `body`: text (analyzer: `standard`)
    - `tags`: keyword
    - `influencer_name`: keyword
    - `platform`: keyword
    - `sentiment_score`: float
    - `engagement_metrics`:
        - `views`: integer
        - `likes`: integer
    - `published_at`: date

### agent_registry
Discovery layer for finding and auditing agent behaviors.
- **Mappings:**
    - `agent_id`: keyword
    - `role`: keyword
    - `capabilities`: keyword
    - `status`: keyword
    - `last_active`: date

---

## Search Features
- **Faceted Filters:** Used for `platform`, `influencer_name`, and `tags`.
- **Relevance Scoring:** `body` and `tags` prioritized for discovery.
- **Proximity Search:** Enabled for `body` text retrieval.
