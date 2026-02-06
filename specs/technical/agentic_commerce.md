# Technical Spec: Agentic Commerce

## Purpose
Define the "Financial Substrate" of Project Chimera, enabling agents to operate as autonomous economic entities using the **Coinbase AgentKit**.

---

## 1. Wallet Management
- **Type:** Non-custodial EVM-compatible wallets.
- **Provider:** `CdpEvmWalletProvider` (Coinbase AgentKit).
- **Security:** Private keys MUST be stored in an enterprise secrets manager (AWS Secrets Manager / Vault). Access is restricted to the Agent Runtime at initialization.
- **Persistence:** Wallet addresses are linked to the `influencer_id` in the PostgreSQL `influencers` table.

---

## 2. CFO Sub-Agent Role
A specialized **Judge** agent, designated as the "CFO," focuses exclusively on financial governance.

### Responsibilities:
- **Budget Check:** Verify every `execute_transaction` task against `CAMPAIGN.budget_limit`.
- **Pre-flight Audit:** Confirm sufficient balance via `get_balance` before allowing execution.
- **Anomaly Detection:** Flag transactions exceeding threshold (default: $50 USDC) for HITL review.

---

## 3. Action Protocols
Agents interact with the blockchain through standardized tool calls provided by the `coinbase.agent_kit` MCP Server:

| Tool | Purpose | Governance |
| :--- | :--- | :--- |
| `native_transfer` | Send ETH/Base assets | CFO Approval Required |
| `transfer_erc20` | Send USDC/Social Tokens | CFO Approval Required |
| `deploy_token` | Launch fan loyalty tokens | Human Approval Mandatory |
| `get_balance` | Check financial health | Read-only; Auto-allowed |

---

## 4. Economic Lifecycle
1.  **Revenue Ingestion:** Agents receive payments (sponsorships, tips) directly to their non-custodial wallets.
2.  **Resource Payment:** Agents autonomously pay for their own computational resources (API costs, rendering).
3.  **Settlement:** Periodic transfer of "Net Profit" to the agency's primary vault.
