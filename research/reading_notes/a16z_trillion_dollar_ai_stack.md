# Reading Notes: a16z Trillion Dollar AI Software Development Stack

## Summary
The article explores how Generative AI is revolutionizing software development, shifting from simple code generation to a **Plan -> Code -> Review** loop. It highlights the emergence of a new "trillion dollar" stack where AI agents are first-class citizens.

## Key Insights
- **The Loop:** Modern AI coding is an iterative process:
    1. **Plan:** LLM drafts specifications and asks for clarifications.
    2. **Code:** Agentic loops generate code and run preliminary tests.
    3. **Review:** Humans or LLMs review the output for alignment with intent.
- **AI-Targeted Docs:** We are moving toward natural language knowledge repositories (e.g., `.cursor/rules`) designed specifically for LLMs rather than humans.
- **Version Control for Agents:** Traditional diffs are losing meaning. Version control is shifting toward tracking **intent**, prompt history, test results, and **agent provenance**.
- **AI QA:** Agents are becoming autonomous QA engineers, crawling UI/API/Backend layers and generating bug reports.
- **Tools for Agents:** 
    - **Code Search:** Essential for large codebases (RAG/parsing).
    - **Sandboxes:** Safe execution environments (E2B, Daytona) are critical to mitigate hallucination and security risks.
    - **Web Search:** Optimized retrieval for ad-hoc external knowledge.

## Implications for Chimera
- **Spec-First is Correct:** Chimera's focus on structured specifications aligns perfectly with the "Plan" phase of the emerging stack.
- **OCC & Provenance:** The requirement for agent provenance and intent-tracking supports our use of Optimistic Concurrency Control and audit logs.
- **MCP first:** The need for specialized search and sandbox tools validates our MCP-first integration strategy.
