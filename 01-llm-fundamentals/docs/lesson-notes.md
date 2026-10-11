# Lesson 01 — Notes and experiments

## Mental model

User text -> build_prompt() -> LLMClient.generate() -> text output.

- **Prompt**: instructions plus task data, not executable code.
- **Inference**: using a trained model to produce an output; not training.
- **Tokens**: model-specific units of input/output used for context and billing.
- **System/developer instructions**: higher-level instructions supplied separately from user content by supported APIs.
- **Mock client**: deterministic stub for tests, not an AI model.

## Experiments

1. Run mock mode and capture output.
2. Make the input blank; observe validation exception.
3. Change the sample email and observe that mock output **does not change**. Explain why.
4. If you have API access, use `--live` and compare results; never save real personal data.

## Questions

1. Why isn't a mock enough to measure extraction quality?
2. What is the difference between `instructions` and `input` in `responses.create`?
3. Why do our tests not need an API key?
4. What happens if an owner or deadline is missing?

## Git history

- `chore: initialize ai engineering labs and first llm client`
