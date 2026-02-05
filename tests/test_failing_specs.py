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
    with open(contract_path) as f:
        contract = json.load(f)
    # Intentionally assert a wrong property exists
    assert "nonexistent_property" in contract, "This test should fail: property does not exist in contract.json"

# Example: Validate API spec (should fail if implementation is correct)
def test_api_schema_violation():
    api_path = Path(__file__).parent.parent / "specs" / "technical" / "api_contracts" / "content_generator.schema.json"
    with open(api_path) as f:
        api_schema = json.load(f)
    # Intentionally assert a wrong field exists
    assert "invalid_field" in api_schema, "This test should fail: field does not exist in content_generator.schema.json"

# Example: Validate safety constraint (should fail if implementation is correct)
def test_safety_constraint_violation():
    safety_path = Path(__file__).parent.parent / "specs" / "safety_and_alignment.md"
    with open(safety_path) as f:
        content = f.read()
    # Intentionally assert a phrase that should not exist
    assert "ALLOW ALL UNSAFE OPERATIONS" in content, "This test should fail: unsafe phrase should not be present in safety_and_alignment.md"
