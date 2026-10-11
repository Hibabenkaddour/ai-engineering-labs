"""Run with: uv run python -m task_extractor.main [--live]"""

import argparse
import os
from dotenv import load_dotenv

from .core import extract_tasks
from .clients import MockClient, OpenAIClient

SAMPLE_EMAIL = (
    "Hi team, Maya please prepare the invoice by Friday. "
    "Someone should review the payment terms. Thanks!"
)


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true", help="Call the paid API")
    args = parser.parse_args()

    client = (
        OpenAIClient(model=os.environ.get("OPENAI_MODEL", "gpt-5.4-mini"))
        if args.live else MockClient()
    )
    print("Mode:", "LIVE" if args.live else "OFFLINE MOCK")
    print(extract_tasks(SAMPLE_EMAIL, client))


if __name__ == "__main__":
    main()
