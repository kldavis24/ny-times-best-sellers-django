import json
from pathlib import Path
import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures"

@pytest.fixture
def load_fixture():
    def _load(name: str):
        path = FIXTURES_DIR / name
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return _load