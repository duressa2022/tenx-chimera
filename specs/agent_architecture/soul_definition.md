# Agent Architecture Spec: SOUL Definition

## Purpose
Define the structure and semantics of the `SOUL.md` file, which serves as the immutable "DNA" and behavioral blueprint for a Project Chimera agent.

---

## 1. File Structure (SOUL.md)
Every agent MUST have a `SOUL.md` file in its configuration root.

### Frontmatter (YAML)
```yaml
id: "agent-uuid"
name: "Persona Name"
niche: "Niche Category (e.g., Tech, Fashion)"
version: "1.0.0"
voice_traits:
  - "Empathetic"
  - "Witty"
  - "Technical"
brand_parameters:
  primary_color: "#HEX"
  typography: "Font Name"
visual_consistency_id: "lora-uuid-or-ref-id"
```

### Body (Markdown)
- **Backstory:** A comprehensive narrative of the agent's origin, expertise, and life experiences.
- **Core Beliefs:** Ethical guardrails and fundamental values (e.g., "Sustainability is non-negotiable").
- **Directives:** Hard constraints on behavior (e.g., "Never discuss political candidates").
- **Vocal Style:** Detailed linguistic markers and slang usage.

---

## 2. Hydration Process
The Agent Runtime hydrates the LLM context using the following lifecycle:

1.  **Parse:** The `SOUL.md` is parsed into a Pydantic model (`AgentPersona`).
2.  **Inject:** Content is mapped to the "Who You Are" section of the system prompt.
3.  **Enforce:** The Judge agent uses the `Directives` section as a checklist for output validation.

---

## 3. Immutability & Governance
- **GitOps:** `SOUL.md` should be version-controlled. Changes require human architect approval.
- **Reflection:** While the agent "learns" (writes to Semantic Memory in Weaviate), the `SOUL.md` remains the static root of truth.
