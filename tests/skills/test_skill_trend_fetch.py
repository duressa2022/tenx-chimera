def test_trend_fetch_contract_shape(skills_dir, load_json):
    contract = load_json(
        skills_dir / "skill_trend_fetch" / "contract.json"
    )

    assert contract["skill_id"] == "skill_trend_fetch"
    assert "input" in contract
    assert "output" in contract
    # failure modes may be documented in spec_reference or additionalProperties

def test_trend_fetch_required_inputs(skills_dir, load_json):
    inputs = load_json(
        skills_dir / "skill_trend_fetch" / "contract.json"
    )["input"]
    props = inputs.get("properties", inputs)

    required = {"source", "niche"}
    assert required.issubset(props.keys())

def test_trend_fetch_output_schema(skills_dir, load_json):
    outputs = load_json(
        skills_dir / "skill_trend_fetch" / "contract.json"
    )["output"]
    props = outputs.get("properties", outputs)

    assert "trend_id" in props
    assert "recommended_content_types" in props
    # recommended_content_types should be an array in the schema
    rct = props.get("recommended_content_types")
    if isinstance(rct, dict):
        assert rct.get("type") == "array"
