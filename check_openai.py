import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Loads .env from the current directory or parent
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    print("🔴 Groq API Key not found in .env file.")
else:
    try:
        client = OpenAI(
            api_key=API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )
        client.models.list()  # This is the actual API call
        print("✅ Groq API Key is working and successfully authenticated!")
    except Exception as e:
        print(f"🔴 Groq API Key test failed: {e}")
