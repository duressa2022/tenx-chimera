REQUIRED_ERROR_CATEGORIES = [
    "ValidationError",
    "ExternalServiceError",
    "RateLimitError",
    "SafetyViolation",
    "RetryExhausted",
]

def test_error_handling_spec_exists(specs_dir):
    assert (specs_dir / "error_handling.md").exists()

def test_error_categories_defined(specs_dir):
    text = (specs_dir / "error_handling.md").read_text(encoding='utf-8')
    for error in REQUIRED_ERROR_CATEGORIES:
        assert error in text, f"Missing error category: {error}"
