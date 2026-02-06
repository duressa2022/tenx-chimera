# OpenClaw Integration Plan

## Purpose
Concise, actionable plan for integrating Chimera skills with the OpenClaw MCP network: adapters, security, provenance, HITL review, testing, and rollout.

---

## Phased Approach

1. Discovery & Contracts (design)
   - Produce contract-to-MCP mapping for each skill (`trend_fetch`, `content_generation`, `engagement_manager`, `publish_content`).
   - Agree on required provenance and human-review fields (`provenance`, `content_meta`, `human_review_ticket`).

2. Security & Identity (foundation)
   - Select auth model (mTLS and/or OAuth2 with signed JWTs). Document required claims and key rotation.
   - Implement identity bootstrapping: issuer, revocation endpoint, and verifier guidelines.

3. Adapter & Middleware (implementation)
   - Build connector library that translates skill requests into MCP payloads and normalizes responses.
   - Provide middleware to attach/validate `provenance`, enforce `risk_classification` rules, and implement idempotency and retry logic.

4. Human-in-the-Loop (HITL) integration
   - Standardize `human_review_ticket` schema and lifecycle (pending → in_review → approved/rejected → closed).
   - Wire skill review queues to OpenClaw review UI or review service; include context: payload, evidence, and provenance.

5. Testing & Sandbox (validation)
   - Create a mock OpenClaw sandbox with signed message examples and test vectors for publish, engagement, and trend flows.
   - Add contract tests (jsonschema) and E2E tests that cover HITL paths and blocked-publish cases.

6. Observability, Monitoring & Trust
   - Emit structured logs and telemetry events (`task.completed`, `safety.violation`, `contract.mismatch`) for trust scoring and audits.
   - Define SLOs and alerts for error rate, latency, and review queue depth.

7. Staged Rollout
   - Canary -> Staging -> Production with feature flags, traffic quotas, and rollback plan.

---

## Key Design Decisions (recommendations)

- Provenance is mandatory for media workflows: include `model_version`, `generated_at`, `source_ids`, and `service_identifiers` in every outbound request.
- Block-first for high risk: any item with `risk_classification == high` must be routed to HITL and not published automatically.
- Idempotency & replay protection: include `idempotency_key`, `nonce`, and `expiry` in message envelopes; require canonical signing rules.
- Error model: classify errors as `transient`, `permanent`, or `policy_block`; connectors should surface these categories to callers.

---

## Minimal Schema/Artifact Deliverables (first sprint)

- Contract mapping doc: table mapping skill `contract.json` → MCP payloads.
- `human_review_ticket.schema.json` — ticket fields and lifecycle states.
- Mock OpenClaw server with sample signed messages and a verifier script.
- JSON Schema unit tests and a CI job to run them.

---

## Operational Runbook Items

- On-call playbook for connector failures: backoff, alerts, and manual retry steps.
- Audit and retention policy for provenance and review artifacts.
- Process for temporarily disabling automated publishes for an agent under probation.

---

If you want, I can (pick one):
- generate the contract mapping doc for the four skills, or
- scaffold the mock OpenClaw server and verifier, or
- add `human_review_ticket.schema.json` and CI test skeleton.
