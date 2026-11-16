import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OMNI_API_KEY")
base_url = os.getenv("OMNI_BASE_URL")
model = os.getenv("OMNI_MODEL")

print("API key loaded:", bool(api_key))
print("Base URL:", base_url)
print("Model:", model)

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
    timeout=60,
    max_retries=0
)

try:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "Explain RAG in two sentences."
            }
        ],
        temperature=0
    )

    print("\nConnection successful!")
    print("Model:", response.model)
    print("Response:", response.choices[0].message.content)

except Exception as e:
    print("\nAPI test failed!")
    print("Exception type:", type(e).__name__)
    print("Error:", repr(e))
