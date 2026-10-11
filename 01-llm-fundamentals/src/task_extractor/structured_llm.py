
import json

from openai import OpenAI
from pydantic import ValidationError

from task_extractor.schemas import TaskExtraction


def extract_tasks(email: str) -> TaskExtraction:
    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",
    )

    response = client.chat.completions.create(
        model="qwen3:1.7b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You extract actionable tasks from business emails. "
                    "Never invent owners or deadlines. "
                    "Use null when information is missing. "
                    "Set priority to medium unless the email "
                    "clearly indicates urgency."
                ),
            },
            {
                "role": "user",
                "content": email,
            },
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "task_extraction",
                "strict": True,
                "schema": TaskExtraction.model_json_schema(),
            },
        },
        extra_body={"think": False},
        temperature=0,
    )

    content = response.choices[0].message.content

    if not content:
        raise ValueError("The model returned an empty response.")

    return TaskExtraction.model_validate_json(content)


def main() -> None:
    email = (
        "Maya, prepare the invoice by Friday. "
        "John, urgently review the payment status tomorrow. "
        "Someone should also verify the contract."
    )

    try:
        result = extract_tasks(email)
        print(json.dumps(result.model_dump(), indent=2))
    except (ValidationError, ValueError) as error:
        print(f"Validation failed: {error}")


if __name__ == "__main__":
    main()
