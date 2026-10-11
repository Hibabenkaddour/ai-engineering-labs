
from openai import OpenAI

# 1. Connect to our local Ollama server
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

# 2. Send a request to Qwen3
response = client.chat.completions.create(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a task extraction assistant. "
                "Extract tasks, owners, and deadlines. "
                "Do not invent information. "
                "Respond concisely."
            ),
        },
        {
            "role": "user",
            "content": (
                "Maya, prepare the invoice by Friday. "
                "John, review the payment status tomorrow."
            ),
        },
    ],
    extra_body={
        "think": False
    },
)

# 3. Display the model's answer
print(response.choices[0].message.content)
