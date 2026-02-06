# Agent Architecture Spec: Human-in-the-Loop

## 1. Purpose
Define the triggers, interfaces, and escalation logic for human intervention within Project Chimera's autonomous swarms.

## 2. Confidence Scoring (NFR 1.0)
Every Worker output MUST be accompanied by a `confidence_score` (float 0.0 to 1.0).
- **Metric:** Derived from LLM log probabilities and Judge validation patterns.
- **Auditability:** The reasoning trace behind the score must be logged in the `ReviewQueue`.

## 3. Automated Escalation Logic (NFR 1.1)
The Judge routing MUST adhere to the following logic tiers:

| Score Range | Tier | Action |
| :--- | :--- | :--- |
| **> 0.90** | High Confidence | **Auto-Approve:** Commit and publish immediately. |
| **0.70 - 0.90** | Medium Confidence | **Async Approval:** Pause task; route to Dashboard HITL queue. |
| **< 0.70** | Low Confidence | **Reject/Retry:** Signal Planner to re-generate with refined prompt. |

## 4. Sensitive Topic Mandatory HITL (NFR 1.2)
Regardless of confidence score, content involving the following topics MUST be routed for human review:
- Politics & Elections
- Health & Medical Advice
- Financial Advice / Speculation
- Legal Claims

## 5. Human Actions
Reviewers utilizing the Orchestrator Dashboard MAY:
- **Approve:** Execute the action immediately.
- **Reject:** Provide feedback and signal a retry.
- **Edit:** Manually correct the agent's output before publishing.
- **Halt:** Temporarily suspend the influencer's lifecycle state.
