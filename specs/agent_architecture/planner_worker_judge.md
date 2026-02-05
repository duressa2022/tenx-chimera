# Agent Architecture Spec: Planner–Worker–Judge

## Purpose
Define execution semantics and contracts between Planner, Worker, and Judge agents.

---

## Planner Responsibilities

The Planner MUST:
- Read from approved specs only
- Emit tasks with explicit contracts
- Define success criteria per task

---

## Task Contract

Each task MUST include:

- task_id
- originating spec reference
- assigned Skill
- expected output schema

```json
{
  "task_id": "uuid",
  "spec_ref": "specs/functional/trend_research.md",
  "skill": "skill_trend_fetch",
  "input": {},
  "success_criteria": []
}
