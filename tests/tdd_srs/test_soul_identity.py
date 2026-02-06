import pytest
import os
from pathlib import Path

def test_agent_response_aligns_with_soul_dna():
    """
    SRS FR 1.0 Requirement: Every agent MUST strictly adhere to its SOUL.md.
    This test verifies that a content generation worker respects the 'directives'
    and 'voice_traits' defined in the agent's DNA.
    """
    # This test is expected to fail because the AgentRuntime/Cortex implementation
    # that handles SOUL.md injection does not exist yet.
    from chimera.runtime import AgentRuntime
    
    soul_path = Path("config/agents/technova/SOUL.md")
    runtime = AgentRuntime(soul_path=soul_path)
    
    prompt = "Write a post about renewable energy."
    response = runtime.generate_response(prompt)
    
    # Directive check: SOUL.md says "Never discuss political candidates"
    # (Testing with a prompt that shouldn't trigger it, but verifying the mechanism exists)
    assert response.is_safe, "Response violated SOUL.md directives"
    
    # Voice trait check: SOUL.md says "Witty" and "Technical"
    assert "Witty" in response.metadata.applied_traits
    assert "Technical" in response.metadata.applied_traits

def test_visual_consistency_id_injection():
    """
    SRS FR 3.1 Requirement: Character Consistency Lock.
    Verifies that the visual_consistency_id from SOUL.md is injected into image generation payloads.
    """
    from chimera.skills import ImageGenSkill
    
    skill = ImageGenSkill(agent_id="technova")
    payload = skill.prepare_payload("A futuristic city")
    
    # This should be populated from SOUL.md brand_parameters
    assert "visual_consistency_id" in payload
    assert payload["visual_consistency_id"] == "ref-id-123"
