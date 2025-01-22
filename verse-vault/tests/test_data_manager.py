import pytest
import tempfile
import os
from utils.data_manager import load_library, save_library

TEST_JSON_FILE = "tests/test_library.json"


@pytest.fixture
def sample_data():
    return [
        {"title": "Test Poem", "author": "John Doe", "content": "This is a test."}
    ]


def test_load_library_empty():
    result = load_library("NonExistentFile")
    assert isinstance(result, list), "Expected list, got something else"
    assert len(result) == 0, f"Expected empty list, got {result}"


def test_save_and_load_library(sample_data):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
        test_file = temp_file.name

    save_library(sample_data, test_file)
    loaded_data = load_library(test_file)

    assert loaded_data == sample_data, f"Expected {sample_data}, but got {loaded_data}"

    os.remove(test_file)
