def test_event_models_defined(specs_dir):
    path = specs_dir / "event_models.md"
    assert path.exists(), "event_models.md is required"

def test_event_models_not_empty(specs_dir):
    content = (specs_dir / "event_models.md").read_text(encoding='utf-8').strip()
    assert len(content) > 300, "Event model spec is suspiciously empty"
