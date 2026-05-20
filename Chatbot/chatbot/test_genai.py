import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

try:
    client = genai.Client(api_key=api_key)
    chat = client.chats.create(model="gemini-2.5-flash")
    resp = chat.send_message("Hello")
    print(resp.text)
except Exception as e:
    print(f"Error: {e}")
