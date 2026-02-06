def test_content_generation_contract_shape(skills_dir, load_json):
    contract = load_json(
        skills_dir / "skill_content_generation" / "contract.json"
    )

    assert contract["skill_id"] == "skill_content_generation"
    assert "input" in contract
    assert "output" in contract

def test_content_generation_inputs(skills_dir, load_json):
    inputs = load_json(
        skills_dir / "skill_content_generation" / "contract.json"
    )["input"]
    props = inputs.get("properties", inputs)

    required = {"trend_id", "content_type", "tone"}
    assert required.issubset(props.keys())

def test_content_generation_outputs(skills_dir, load_json):
    outputs = load_json(
        skills_dir / "skill_content_generation" / "contract.json"
    )["output"]
    props = outputs.get("properties", outputs)

    assert "content_id" in props
    assert "result" in props
