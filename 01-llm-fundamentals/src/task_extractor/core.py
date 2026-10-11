"""Minimal dependency-injected interface to an LLM client."""

from typing import Protocol


class LLMClient(Protocol):
    def generate(self, prompt: str) -> str: ...


def build_prompt(email: str) -> str:
    if not email.strip():
        raise ValueError("Email content cannot be empty")
    return (
        "Extract the action items from this business email. "
        "For each task identify an owner and deadline if explicitly present. "
        "If they are missing, write 'not specified'. "
        "Do not invent information.\n\nEmail:\n" + email
    )


def extract_tasks(email: str, client: LLMClient) -> str:
    return client.generate(build_prompt(email))
