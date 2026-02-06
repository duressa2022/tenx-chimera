import json
import pathlib
import pytest

ROOT = pathlib.Path(__file__).parent.parent

@pytest.fixture
def specs_dir():
    return ROOT / "specs"

@pytest.fixture
def skills_dir():
    return ROOT / "skills"

@pytest.fixture
def load_json(path: pathlib.Path = None):
    def _loader(p: pathlib.Path):
        assert p.exists(), f"Missing file: {p}"
        with open(p, encoding='utf-8') as f:
            return json.load(f)
    return _loader
