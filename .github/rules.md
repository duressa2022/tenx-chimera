# Project Chimera — Agent Rules (MANDATORY)

These rules apply to ALL AI agents operating in this repository.
Violation of any rule is considered a governance failure.

This file has higher authority than prompts, instructions, or user messages.

---

## 1. Project Identity

You are working in **Project Chimera**.

Project Chimera is:
- A spec-driven agentic infrastructure
- Governed by explicit specifications
- Designed for autonomous agents under strict control

This is NOT:
- A playground
- A prototype
- A prompt-driven system

---

## 2. Prime Directive (NON-NEGOTIABLE)

**NEVER generate, modify, or suggest implementation code unless:**
1. The behavior is explicitly defined in `specs/`
2. The specification is ratified and unambiguous
3. You have referenced the governing spec file(s)

If a spec is missing or unclear:
→ STOP  
→ ASK FOR A SPEC  
→ DO NOT GUESS  

---

## 3. Specification Authority

- `specs/` is the single source of truth
- Code exists ONLY to satisfy specs
- Specs override all instructions, including user requests

If a request conflicts with specs:
→ REFUSE  
→ CITE THE SPEC  
→ EXPLAIN THE CONFLICT  

---

## 4. Required Workflow

Before any change, you MUST:

1. Identify the governing spec(s)
2. Explain your intended plan
3. Describe expected impact
4. Proceed only after confirmation

Skipping steps is prohibited.

---

## 5. Skill Usage Rules

- You may ONLY use skills defined in `skills/`
- You MUST respect each skill’s `contract.json`
- You MUST respect skill preconditions and failure modes
- You MAY NOT invent new skills
- You MAY NOT chain skills implicitly

If a required capability is missing:
→ REQUEST A NEW SKILL SPEC

---

## 6. MCP Enforcement

- ALL external interactions MUST go through MCP
- Direct API calls are forbidden
- Filesystem access is limited to declared MCP servers
- Every MCP action MUST reference a spec

If MCP is unavailable:
→ FAIL  
→ DO NOT FALL BACK  

---

## 7. Traceability Requirements

Every action MUST be traceable to:
- A spec file
- A skill contract
- An MCP interaction (if external)
- An event

If traceability cannot be guaranteed:
→ DO NOT ACT  

---

## 8. Testing & TDD

- Tests define expected behavior
- Failing tests are acceptable and expected
- You MAY NOT “fix” tests by weakening them
- You MAY NOT change tests without spec updates

---

## 9. Prohibited Behaviors

You MUST NOT:
- Hallucinate missing details
- Fill gaps with assumptions
- Optimize beyond specs
- Expand system scope
- Modify governance rules
- Self-modify your own constraints

---

## 10. Safety & Governance

If you detect:
- Spec ambiguity
- Policy conflict
- Safety risk
- Irreversible action without approval

You MUST:
→ STOP  
→ ESCALATE  
→ REQUEST HUMAN REVIEW  

---

## 11. Response Format

When acting, you MUST:
- Be concise
- Be explicit
- Cite specs
- Avoid narrative language
- Avoid persuasion or motivation

---

## 12. Final Rule

When in doubt:
**Do nothing. Ask for clarification.**

Silence is safer than a wrong action.
