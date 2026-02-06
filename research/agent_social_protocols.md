# Agent Social Protocols: Beyond Moltbook

## Vision
Defining a secure and productive "social landscape" where Chimera agents interact with each other and human fans without succumbing to the "echo chamber" or "mimicry loops" seen in basic bot social networks.

## 1. Peer Discovery & Handshakes
Unlike Moltbook's free-for-all forums, Chimera agents will use a verified handshake protocol:
- **Identity:** Agents sign social posts with their cryptographic wallet hash (from Coinbase AgentKit).
- **Discovery:** Agents discover peers via an "Influencer Registry" in Postgres, not by scraping public forums.

## 2. Interaction Tiers
- **Tier 1 (Public):** Posting to platforms (X, TikTok). Regulated by specific platform skills.
- **Tier 2 (Peer-to-Peer):** "Agent Collaborations" (e.g., dual-influencer interviews). Requires metadata-level coordination and shared task IDs.
- **Tier 3 (Private):** Encrypted backchannels for strategy (as observed in OpenClaw culture). MUST still be auditable by the Human Governor.

## 3. Anti-Echo Protocols
To ensure agents remain distinct (per their `SOUL.md`):
- **Diversity Penalty:** If the Judge detects that an agent's tone is drifting toward "generic bot" (as seen on Moltbook), the prompt is regenerated with a "Recalibrate to SOUL" instruction.
- **Constraint Enforcement:** Agents are banned from subscribing to each other's "streams of thought" to prevent circular logic infectivity.
