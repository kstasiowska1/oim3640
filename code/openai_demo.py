# OpenAI
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
client = OpenAI()  # reads OPENAI_API_KEY from .env

response = client.responses.create(
    model="gpt-5-nano",
    input="write a haiku about the ocean"
    )

print(response.output_text)
