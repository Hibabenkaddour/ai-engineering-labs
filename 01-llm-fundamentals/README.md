# Lab 01 — LLM API Fundamentals

**Goal:** Understand prompts, API requests, model responses, mocking, and test isolation without relying on a framework.

## Setup (from this folder)

1. Install Python 3.11+ and [uv](https://docs.astral.sh/uv/getting-started/installation/).
2. `uv sync --extra dev`
3. `uv run python -m task_extractor.main` — offline deterministic demo; no key or costs.
4. `uv run pytest -v` — unit tests (mocked; no network requests).

## Optional real API call

Copy `.env.example` to `.env` and replace the example key with your own secret key, and set `OPENAI_MODEL` to a model accessible to your API account. Then run:

`uv run python -m task_extractor.main --live`

**API usage may incur charges.** ChatGPT subscriptions do not automatically include API credits. Don't commit `.env`.

## Files

- `src/task_extractor/core.py`: prompt construction and injectable LLM client contract.
- `src/task_extractor/clients.py`: offline mock and OpenAI Responses API client.
- `src/task_extractor/main.py`: CLI entrypoint.
- `tests/test_core.py`: tests, all offline.
- `docs/lesson-notes.md`: learning notes and experiments.

## Why the mock?

The deterministic mock allows unit tests to check Python control flow without depending on live API availability, fees, or model output variability. **It does not test model quality.**

## Next feature

After understanding the API call, add Pydantic structured outputs and validate extracted task objects; then implement tool calling.
