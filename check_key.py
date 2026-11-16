import os
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    print("GROQ_API_KEY not found in .env")
else:
    try:
        client = OpenAI(
            api_key=API_KEY,
            base_url="https://api.groq.com/openai/v1",
        )
        client.models.list()  # simple test call
        print("Groq API key is valid and works!")
    except Exception as e:
        print(f"Groq API key test failed: {e}")