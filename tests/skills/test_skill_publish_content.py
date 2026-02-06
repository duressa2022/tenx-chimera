def test_publish_content_contract_shape(skills_dir, load_json):
    contract = load_json(
        skills_dir / "skill_publish_content" / "contract.json"
    )

    assert contract["skill_id"] == "skill_publish_content"
    assert "input" in contract
    assert "output" in contract
    # platform policies may be described in the spec_reference or description

def test_publish_content_required_inputs(skills_dir, load_json):
    inputs = load_json(
        skills_dir / "skill_publish_content" / "contract.json"
    )["input"]
    props = inputs.get("properties", inputs)

    required = {"content_id", "content_type", "platform"}
    assert required.issubset(props.keys())

def test_publish_content_outputs(skills_dir, load_json):
    outputs = load_json(
        skills_dir / "skill_publish_content" / "contract.json"
    )["output"]
    props = outputs.get("properties", outputs)

    assert "publish_id" in props
    assert "status" in props
