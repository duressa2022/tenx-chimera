# Contributing to Project Chimera

## 📜 Governance-First Contribution
Project Chimera uses **Spec-Driven Development (SDD)**. Every change must be preceded by a ratified specification and a failing test case that defines the target behavior.

## Scope

This document defines **how contributions are evaluated and accepted**.
It applies equally to human contributors and AI agents.

---

## Contribution Order (Mandatory)

Contributions MUST follow this order:

1. Specification change (`specs/`)
2. Test definition (`tests/`)
3. Implementation (if applicable)

Any contribution that skips a step will be rejected.

---

## Security Policy — Project Chimera

## Scope
This policy covers the autonomous influencer factory, including:
- **Agent Behavior:** Sandboxing and intent validation.
- **Skill Execution:** Schema-validated input/output.
- **External Integrations:** MCP-only data ingress/egress.
- **Data Handling:** Secure metadata processing and commerce.

---

## What You MAY Contribute

- Specifications
- Skill contracts
- Tests
- Governance configuration
- Documentation clarifying intent

---

## What You MAY NOT Contribute

- Implementation without specs
- Prompt-based behavior
- Unspecified agent logic
- Self-modifying systems
- Bypasses of governance or MCP

---

## Pull Request Requirements

Every PR MUST include:

- Reference to affected spec file(s)
- Rationale for the change
- Impact analysis (safety, governance, agents)
- Tests (if behavior changes)

---

## Review Rules

- Specs are reviewed before code
- Failing tests are acceptable if intentional
- Governance violations block merges
- CI must pass unless explicitly waived by maintainers

---

## AI Contributions

AI-generated contributions are allowed **only if**:
- They follow all specs
- They explain intent before changes
- They do not introduce ambiguity

Unattributed AI changes are treated as violations.
