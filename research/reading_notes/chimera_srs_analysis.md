# Research Note: Chimera SRS Analysis

## Context
This note bridges the gap between the project's **Software Requirements Specification (SRS)** and the external research conducted.

## Strategic Alignment
- **Swarm Architecture:** The SRS calls for a "Hierarchical Swarm" (Planner-Worker-Judge). Research (a16z) confirms this is now the standard "industry-grade" loop for reliable agentic systems.
- **Persistence:** The SRS's polyglot approach (Weaviate + Postgres + Redis) aligns with the "Tools for Agents" market map, specifically the need for specialized vector search (Weaviate) and low-latency cache (Redis).
- **Agentic Commerce:** Integrating Coinbase AgentKit as a "Financial Substrate" puts Chimera ahead of pure automation tools, moving it into the "Economic Agency" category.

## Identified Gaps (from Research)
- **Agent Provenance:** We have audit logs, but we could improve how we track the "intent" vs "code change" relationship, as suggested by a16z.
- **AI-Optimized Knowledge:** Our `specs/` are good, but we should consider a dedicated `rules/` or `.cursor/rules` directory to explicitly guide the AI's "internal" decision-making, separate from the project specs.
- **Social Protocol:** While we have functional specs for engagement, we haven't yet defined a protocol for **agent-to-agent** interaction (e.g., a Chimera-specific "Moltbook" or peer-discovery mechanism).

## Recommended Pivot/Refinement
- **Strengthen the "Judge":** Given the vulnerability findings in OpenClaw, our Judge agents must be even more robust, specifically checking for malicious prompts and indirect injection.
- **Character Consistency:** The SRS mentions "Character Consistency Lock." Based on research, this should be implemented as a "Visual SOUL" skill that agents must call before any media generation.
