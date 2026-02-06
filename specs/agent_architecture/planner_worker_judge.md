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

## State Consistency & OCC (FR 6.1)

The system SHALL use **Optimistic Concurrency Control (OCC)** to ensure data integrity in the high-velocity swarm.

### Versioning
Every `GlobalState` update MUST increment a `state_version` (hash or timestamp).

### The OCC Loop
1.  **Read:** Worker starts a task with a snapshot of the current `state_version`.
2.  **Execute:** Worker performs the task (e.g., drafts content).
3.  **Commit:** Judge attempts to result the task.
4.  **Validate:** Judge checks if the `state_version` in the database matches the snapshot the Worker started with.
5.  **Fault handling:**
    - If Match: Commit succeeds; `state_version` increments.
    - If Mismatch: Commit FAILS. Judge invalidates the result and re-queues the task for the Planner.

---

## Task Contract

Each task MUST include:
- task_id
- state_version (at time of creation)
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
