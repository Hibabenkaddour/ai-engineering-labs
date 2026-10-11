import pytest
from task_extractor.clients import MockClient
from task_extractor.core import build_prompt, extract_tasks


def test_blank_email_is_rejected():
    with pytest.raises(ValueError, match="cannot be empty"):
        build_prompt("  ")


def test_prompt_preserves_email():
    assert "Maya to prepare invoice" in build_prompt("Maya to prepare invoice")


def test_mock_extracts_expected_text():
    result = extract_tasks("Maya prepares invoice", MockClient())
    assert "Maya" in result


def test_client_is_called_with_prompt():
    class RecordingClient:
        def __init__(self):
            self.prompt = ""
        def generate(self, prompt: str) -> str:
            self.prompt = prompt
            return "Done"
    client = RecordingClient()
    assert extract_tasks("Send report", client) == "Done"
    assert "Send report" in client.prompt
