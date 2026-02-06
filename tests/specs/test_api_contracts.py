import jsonschema
from pathlib import Path

API_SCHEMAS = [
    "trend_fetcher.schema.json",
    "content_generator.schema.json",
    "publisher.schema.json",
    "analytics_collector.schema.json",
]

def test_api_schemas_exist(specs_dir):
    api_dir = specs_dir / "api_contracts"
    for schema in API_SCHEMAS:
        assert (api_dir / schema).exists(), f"Missing API schema: {schema}"

def test_api_schemas_are_valid_json(specs_dir, load_json):
    api_dir = specs_dir / "api_contracts"
    for schema in API_SCHEMAS:
        data = load_json(api_dir / schema)
        jsonschema.Draft7Validator.check_schema(data)
