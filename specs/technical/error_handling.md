
---

# 📄 `specs/technical/error_handling.md`

```md
# Error Handling & Failure Semantics — Project Chimera

## Purpose

This document defines how Chimera reacts to failures, violations,
and uncertainty—especially under autonomous operation.

Failure handling is a **first-class system behavior**, not an afterthought.

---

## Core Philosophy

- Fail fast
- Fail loudly
- Fail safely
- Never guess

If the system is unsure, it must stop and ask.

---

## Error Classification

All errors MUST be classified into exactly one category.

---

## 1. Recoverable Errors

### Definition
Errors caused by temporary or external conditions.

### Examples
- MCP server timeout
- Rate limiting
- Temporary platform unavailability

### Agent Response
- Retry with bounded attempts
- Emit error event
- Escalate if retries exhausted

### System Behavior
- No state mutation
- No content publishing
- No silent degradation

---

## 2. Non-Recoverable Errors

### Definition
Errors caused by violations of specs, contracts, or invariants.

### Examples
- Skill input schema mismatch
- Invalid lifecycle state
- Missing approval

### Agent Response
- Immediate task termination
- Emit error event
- Recommend suspension if repeated

### System Behavior
- Block downstream actions
- Require human review for resumption

---

## 3. Safety-Critical Errors

### Definition
Errors that could result in harm, policy violations,
or loss of trust.

### Examples
- Ambiguous content policy classification
- Potential misinformation
- Unexpected agent behavior

### Agent Response
- Halt execution
- Emit safety error event
- Request Human-in-the-Loop

### System Behavior
- Suspend influencer
- Lock publishing pipeline
- Preserve all context for review

---

## Mandatory Error Payload

Every error event MUST include:

```json
{
  "error_type": "string",
  "severity": "low | medium | high | critical",
  "affected_entity": "agent | influencer | content | skill",
  "description": "string",
  "spec_reference": "string"
}
