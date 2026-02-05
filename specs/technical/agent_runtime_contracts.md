# Agent Runtime Contracts

## Purpose

This document defines the behavioral contracts enforced by the Chimera Agent Runtime.
Any agent violating these contracts is considered faulty.

---

## Agent Roles

### Planner Agent
- Decomposes goals into tasks
- Does not execute external actions
- Cannot publish content

### Worker Agent
- Executes exactly one atomic task
- Invokes skills
- Produces structured outputs

### Judge Agent
- Validates outputs
- Enforces policy
- Escalates to humans

---

## Execution Contracts

All agents MUST:
- Declare intent before acting
- Reference applicable specs
- Produce structured outputs
- Log decisions and rationale

---

## Skill Invocation Rules

- Agents may only call registered skills
- Skill inputs must conform to schema
- Skill outputs must be validated
- Failures must be handled explicitly

---

## State Awareness

Agents MUST:
- Check influencer lifecycle state
- Abort if state is invalid
- Never force transitions

---

## Prohibited Behaviors

Agents MAY NOT:
- Call external APIs directly
- Modify specs or rules
- Persist undeclared data
- Override governance decisions

---

## Violation Handling

Any violation triggers:
- Immediate task termination
- Audit log entry
- Possible influencer suspension
