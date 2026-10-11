"""Deterministic mock and real OpenAI API adapters."""

from openai import OpenAI


class MockClient:
    """Predictable offline response; NOT a language model."""

    def generate(self, prompt: str) -> str:
        return "Task: Prepare invoice | Owner: Maya | Deadline: Friday"


class OpenAIClient:
    def __init__(self, model: str) -> None:
        self.client = OpenAI()  # Reads OPENAI_API_KEY from environment
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            instructions="You extract tasks accurately. Never invent owners or deadlines.",
            input=prompt,
            store=False,
        )
        if not response.output_text:
            raise RuntimeError("Model returned no text")
        return response.output_text
