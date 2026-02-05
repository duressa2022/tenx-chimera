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

---

### Publishing
The system MUST:
- Publish content via MCP only
- Capture platform response metadata
- Retry failed publishes safely

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

---

## Failure Modes

- Platform rejection → retry or escalate
- Credential failure → hard stop
- Unexpected response → Judge review
