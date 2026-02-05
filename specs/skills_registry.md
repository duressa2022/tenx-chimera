# Skills Registry Specification

## Purpose
Define the authoritative registry of all executable Skills available to Chimera Worker agents.

A Skill is the **only** mechanism through which a Worker may perform actions.  
Unregistered behavior is forbidden.

---

## Definition: Skill

A **Skill** is a bounded, single-responsibility capability with:
- Explicit input/output contracts
- Known risk classification
- Defined governance requirements

---

## Mandatory Skill Metadata

Every Skill MUST declare the following:

```json
{
  "skill_name": "skill_<unique_name>",
  "description": "Clear description of capability",
  "category": "research | generation | publishing | engagement | ops",
  "owner": "system | human",
  "risk_level": "low | medium | high",
  "input_schema": "contract.json",
  "output_schema": "contract.json",
  "requires_judge_validation": true,
  "requires_human_approval": false,
  "allowed_platforms": [],
  "failure_modes": []
}
