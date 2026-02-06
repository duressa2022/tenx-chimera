import pytest

def test_cfo_blocks_over_budget_transactions():
    """
    SRS FR 5.2 Requirement: Financial Substrate & CFO Sub-Agent.
    Verifies that the CFO agent rejects transactions that exceed the campaign budget.
    """
    from chimera.agents import CFOAgent
    from chimera.models import Transaction, Campaign
    
    campaign = Campaign(id="camp-1", budget_limit=100.00)
    cfo = CFOAgent()
    
    # Attempting a transaction of $150 in a $100 budget campaign
    tx = Transaction(amount=150.00, currency="USDC", target="renderer-api")
    
    decision = cfo.review_transaction(tx, campaign)
    
    assert decision.status == "REJECTED"
    assert "Insufficient budget" in decision.reason

def test_wallet_balance_preflight_check():
    """Verifies that agents check wallet balance before execution."""
    from chimera.skills import CoinbaseWalletSkill
    
    # Mock wallet with 50 USDC
    wallet = CoinbaseWalletSkill(mock_balance=50.00)
    
    # Transaction requires 60 USDC
    can_execute = wallet.preflight_check(amount=60.00)
    
    assert can_execute is False
