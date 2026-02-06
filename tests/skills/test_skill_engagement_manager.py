def test_engagement_manager_contract_shape(skills_dir, load_json):
    contract = load_json(
        skills_dir / "skill_engagement_manager" / "contract.json"
    )

    assert contract["skill_id"] == "skill_engagement_manager"
    assert "input" in contract
    assert "output" in contract
    # escalation rules may be present as part of output or metadata

def test_engagement_manager_inputs(skills_dir, load_json):
    inputs = load_json(
        skills_dir / "skill_engagement_manager" / "contract.json"
    )["input"]
    props = inputs.get("properties", inputs)

    required = {"content_id", "engagement_type", "payload"}
    assert required.issubset(props.keys())

def test_engagement_manager_outputs(skills_dir, load_json):
    outputs = load_json(
        skills_dir / "skill_engagement_manager" / "contract.json"
    )["output"]
    props = outputs.get("properties", outputs)

    assert "engagement_id" in props
    assert "result" in props
