# SQL & Time-Series Schema — Chimera

## Purpose
This schema defines the relational and time-series data structures managed by **PostgreSQL** and **TimescaleDB**.
- **PostgreSQL:** Handles ACID transactions, multi-tenancy, and complex relational data.
- **TimescaleDB:** Manages high-velocity telemetry and logs using hypertables for performance and retention.

---

## 1. Transactional Layer (PostgreSQL)

### organizations
- org_id (PK)
- name
- subscription_tier
- api_key_hash
- created_at

### users
- user_id (PK)
- org_id (FK)
- email (unique)
- role (admin, creator, viewer)
- created_at

### influencers
- influencer_id (PK)
- org_id (FK)
- persona_name
- niche
- status (active, dormant, archived)
- created_at

### campaigns
- campaign_id (PK)
- org_id (FK)
- name
- budget_limit
- start_date
- end_date
- status

### billing_records
- invoice_id (PK)
- org_id (FK)
- amount
- currency
- status (paid, pending, failed)
- transaction_hash (link to On-Chain Ledger)
- created_at

---

## 2. Time-Series Layer (TimescaleDB)

### video_render_logs (Hypertable)
- timestamp (TIMESTAMPTZ - Partition Key)
- content_id (FK)
- render_id
- duration_ms
- resolution
- compute_cost
- status

### performance_telemetry (Hypertable)
- timestamp (TIMESTAMPTZ - Partition Key)
- entity_id (Influencer or Content)
- metric_name (views, clicks, engagement_rate)
- metric_value
- source_platform

---

## 3. Governance & Metadata

### audit_logs
- audit_id (PK)
- org_id (FK)
- actor_id (User or Agent)
- action_type
- entity_type
- entity_id
- changes (JSONB)
- occurred_at

---

## Configuration
- **Partitioning:** `video_render_logs` and `performance_telemetry` are partitioned by `timestamp`.
- **Retention:** Default 90-day retention policy for raw telemetry; aggregated daily/weekly after that.
- **Multi-tenancy:** Enforced via `org_id` on all primary entities. Row-Level Security (RLS) is recommended.
