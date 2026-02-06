# Governance Model — Project Chimera

## Purpose

This document defines how authority, responsibility,
and escalation function within Project Chimera.

Governance is **enforced**, not advisory.

---

## Authority Layers

### 1. Specifications (Highest Authority)
- Define system intent
- Cannot be overridden by code
- Changes require human approval

---

### 2. Governance Automation
- CI/CD
- Test enforcement
- AI review tools (e.g., CodeRabbit)

Automation enforces specs mechanically.

---

### 3. Human Oversight
- Final approval for:
  - Spec changes
  - Safety exceptions
  - High-risk behavior

---

## Agent Authority (Strictly Limited)

Agents MAY:
- Execute skills
- Propose changes
- Generate code under specs

Agents MAY NOT:
- Change specs
- Bypass tests
- Override governance
- Self-expand capabilities

---

## Decision Escalation

Escalation is REQUIRED when:
- Specs conflict
- Safety is ambiguous
- Irreversible actions fail
- Repeated violations occur

Escalation target:
- Human maintainers

---

## Enforcement

Governance violations result in:
- Blocked merges
- Agent suspension
- Repository lockdown (if necessary)

Governance decisions are final.
