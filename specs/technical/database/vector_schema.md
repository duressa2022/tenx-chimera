# Vector Schema — Weaviate

## Purpose
Define the vector-native data structures for **Weaviate**. This schema supports RAG (Retrieval-Augmented Generation), semantic search, and agent memory management.

---

## Classes

### AgentPersona
Stores the core definition and behavioral constraints of an influencer.
- **Properties:**
    - `personaName`: string (indexed)
    - `niche`: string
    - `coreTraits`: text
    - `vocalStyle`: text
    - `forbiddenTopics`: string[]
- **Vectorizer:** `text2vec-openai` (or `text2vec-cohere`)
- **Module Config:**
    - `distanceMetric`: `cosine`

### SemanticMemory
Long-term memory storage used for contextual retrieval during RAG.
- **Properties:**
    - `influencerId`: string (cross-reference)
    - `content`: text
    - `memoryType`: string (reflection, observation, goal)
    - `importance`: number (0.0 to 1.0)
    - `timestamp`: date
- **Vectorizer:** `text2vec-openai`
- **Searchability:** Optimized for vector similarity search.

### InteractionFragment
Short-to-medium term context from user interactions.
- **Properties:**
    - `sessionId`: string
    - `agentRole`: string (user, assistant)
    - `text`: text
    - `timestamp`: date
- **Vectorizer:** `text2vec-openai`

---

## Multi-Tenancy
- **Strategy:** Class-level isolation or multi-tenant headers.
- **Implementation:** Each class uses `multiTenancyConfig: { "enabled": true }` to ensure data isolation between different influencers/organizations.
