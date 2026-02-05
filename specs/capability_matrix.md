
---

# `capability_matrix.md`

```md
# Capability Matrix Specification

## Purpose
Define which agent roles may perform which capabilities, enforcing separation of concerns.

---

## Agent Roles

- Planner Agent
- Worker Agent
- Judge Agent
- Human Operator

---

## Capability Categories

- Planning
- Execution
- Validation
- Escalation
- Governance
- System Control

---

## Capability Matrix

| Capability                     | Planner | Worker | Judge | Human |
|--------------------------------|---------|--------|-------|-------|
| Read Specs                     | ✅      | ❌     | ✅    | ✅    |
| Create Task Plans              | ✅      | ❌     | ❌    | ❌    |
| Execute Skills                 | ❌      | ✅     | ❌    | ❌    |
| Validate Outputs               | ❌      | ❌     | ✅    | ✅    |
| Retry / Reject Tasks           | ❌      | ❌     | ✅    | ❌    |
| Escalate to Human              | ❌      | ❌     | ✅    | ❌    |
| Override Decisions             | ❌      | ❌     | ❌    | ✅    |
| Modify Policies / Specs        | ❌      | ❌     | ❌    | ✅    |
| Emergency Kill Switch          | ❌      | ❌     | ❌    | ✅    |

---

## Enforcement Rules

The system MUST:
- Enforce this matrix at runtime
- Log all capability violations
- Halt execution on repeated violations

Agents MUST NOT:
- Act outside assigned capabilities
- Escalate without authorization

---

## Failure Modes

- Capability breach → Immediate halt
- Unauthorized escalation → Judge suspension
- Role confusion → System pause
