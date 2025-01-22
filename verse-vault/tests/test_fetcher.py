import pytest
import json
import os
import tempfile
from unittest.mock import patch
from utils.fetcher import fetch_by_title
from utils.data_manager import load_all_libraries


@pytest.fixture
def mock_library_data():
    """Provides mock library data."""
    return [
        {"title": "A Short Tale", "author": "Writer X", "content": "A story.", "type": "Poem"}
    ]


@pytest.fixture
def mock_library_file(mock_library_data):
    """Creates a temporary JSON file with mock data."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
        temp_filename = temp_file.name
        with open(temp_filename, "w", encoding="utf-8") as f:
            json.dump(mock_library_data, f)

    yield temp_filename
    os.remove(temp_filename)


def test_fetch_by_title(mock_library_data):
    """Test fetching an entry by title using mocked data."""
    with patch("utils.fetcher.load_all_libraries", return_value=mock_library_data):
        result = fetch_by_title("A Short Tale", "Poem")

    assert result is not None, "Expected a valid entry, but got None"
    assert result["title"] == "A Short Tale", "Title mismatch in fetched result"
    assert result["content"] == "A story.", "Incorrect content fetched"
