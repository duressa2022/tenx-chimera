"""
Failing schema validation tests for contract and API specs.
These tests are designed to fail by design, to ensure that the implementation cannot drift from the schema and spec requirements.
"""
import json
import pytest
from pathlib import Path

# Example: Validate contract.json schemas (should fail if implementation is correct)
def test_contract_schema_violation():
    contract_path = Path(__file__).parent.parent / "skills" / "skill_content_generation" / "contract.json"
    with open(contract_path, encoding='utf-8') as f:
        contract = json.load(f)
    # Validate contract contains expected top-level keys and required input properties
    assert "skill_id" in contract
    assert "input" in contract and "output" in contract
    input_props = contract.get("input", {}).get("properties", {})
    for key in ("trend_id", "content_type", "tone"):
        assert key in input_props, f"Missing expected input property: {key}"

# Example: Validate API spec (should fail if implementation is correct)
def test_api_schema_violation():
    api_path = Path(__file__).parent.parent / "specs" / "technical" / "api_contracts" / "content_generator.schema.json"
    with open(api_path, encoding='utf-8') as f:
        api_schema = json.load(f)
    # Ensure schema declares required output fields for content generator
    req = api_schema.get("required", [])
    for field in ("content_id", "trend_id", "content_type", "risk_classification"):
        assert field in req, f"Schema missing required field: {field}"

# Example: Validate safety constraint (should fail if implementation is correct)
def test_safety_constraint_violation():
    safety_path = Path(__file__).parent.parent / "specs" / "safety_and_alignment.md"
    with open(safety_path, encoding='utf-8') as f:
        content = f.read()
    # Ensure safety doc contains key policy statements
    assert "The system MUST NEVER" in content or "Prohibited Actions" in content
    assert "Escalation Triggers" in content or "Escalation is REQUIRED" in content
