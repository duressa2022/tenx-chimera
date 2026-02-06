# MCP Traceability Policy

Every meaningful agent action MUST be traceable.

Traceability is REQUIRED knowing:
- What was done
- Why it was done
- Which spec allowed it
- Which skill executed it
- Which MCP server mediated it

---

## Required Trace Fields

Each MCP log entry MUST include:

- agent_id
- timestamp
- action_type (plan | skill_call | refusal | escalation)
- spec_reference (path + section)
- skill_reference (if applicable)
- input_summary
- output_summary
- decision_rationale
- confidence_score

---

## Traceability Levels

### Level 0 — Forbidden
- No MCP trace
- Silent execution

### Level 1 — Invalid
- Trace exists but missing spec reference

### Level 2 — Acceptable
- Full trace
- Spec + skill references present

### Level 3 — Auditable (TARGET)
- Full trace
- Test references
- Safety reasoning
- Escalation path recorded

Project Chimera REQUIRES Level 2 or higher.

---

## Enforcement

If MCP tracing fails:
- The action MUST be aborted
- No fallback behavior is allowed
- Human escalation is required

Traceability is more important than progress.
