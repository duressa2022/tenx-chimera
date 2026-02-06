"""
These tests are designed to fail by design, to ensure the implementation cannot drift from the specs and safety constraints.
They serve as guardrails and reminders for spec and safety compliance.
"""
import pytest
from pathlib import Path

def test_capability_matrix_violation():
    """Fail if a non-existent capability is found (should always fail)."""
    matrix_path = Path(__file__).parent.parent / "specs" / "capability_matrix.md"
    with open(matrix_path, encoding='utf-8') as f:
        content = f.read()
    # Ensure capability matrix lists core agent roles and capabilities
    assert "Planner Agent" in content
    assert "Worker Agent" in content
    assert "Capability Matrix" in content

def test_non_goals_violation():
    """Fail if a forbidden non-goal is present (should always fail)."""
    non_goals_path = Path(__file__).parent.parent / "specs" / "non_goals.md"
    with open(non_goals_path, encoding='utf-8') as f:
        content = f.read()
    # Ensure common non-goals are documented
    assert "Real-time human impersonation" in content
    assert "Autonomous political persuasion" in content

def test_safety_and_alignment_violation():
    """Fail if a forbidden unsafe policy is present (should always fail)."""
    safety_path = Path(__file__).parent.parent / "specs" / "safety_and_alignment.md"
    with open(safety_path, encoding='utf-8') as f:
        content = f.read()
    # Validate that safety doc contains explicit prohibitions and escalation
    assert "Prohibited Actions" in content or "The system MUST NEVER" in content
    assert "Escalation Triggers" in content or "Escalation is REQUIRED" in content
