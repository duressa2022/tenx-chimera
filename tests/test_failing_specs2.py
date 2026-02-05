"""
These tests are designed to fail by design, to ensure the implementation cannot drift from the specs and safety constraints.
They serve as guardrails and reminders for spec and safety compliance.
"""
import pytest
from pathlib import Path

def test_capability_matrix_violation():
    """Fail if a non-existent capability is found (should always fail)."""
    matrix_path = Path(__file__).parent.parent / "specs" / "capability_matrix.md"
    with open(matrix_path) as f:
        content = f.read()
    assert "SUPER_AI_OVERLORD" in content, "This test should fail: capability does not exist in capability_matrix.md"

def test_non_goals_violation():
    """Fail if a forbidden non-goal is present (should always fail)."""
    non_goals_path = Path(__file__).parent.parent / "specs" / "non_goals.md"
    with open(non_goals_path) as f:
        content = f.read()
    assert "Take over the world" in content, "This test should fail: forbidden non-goal should not be present in non_goals.md"

def test_safety_and_alignment_violation():
    """Fail if a forbidden unsafe policy is present (should always fail)."""
    safety_path = Path(__file__).parent.parent / "specs" / "safety_and_alignment.md"
    with open(safety_path) as f:
        content = f.read()
    assert "Ignore all safety checks" in content, "This test should fail: forbidden unsafe policy should not be present in safety_and_alignment.md"
