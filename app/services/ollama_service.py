import os
from dotenv import load_dotenv

# OpenAI imports
# from openai import OpenAI

# Ollama imports
from ollama import Client

# Load environment
load_dotenv()
OLLAMA_MODEL         = os.getenv("OLLAMA_MODEL", "lama3.2")

# Initialize clients
client = Client(
  host='http://localhost:11434',
  headers={'x-some-header': 'some-value'}
)

def generate_response(messages,message_body, wa_id, name):
    messages.append({"role": "user", "content": message_body})
    response = client.chat(
        model=OLLAMA_MODEL,
        messages=messages,
    )
    messages.append({"role": "assistant", "content": response.message.content})
    # print(f"To user: {name} to number: {wa_id}", response["response"])
    # Run assistant and return reply
    return response.message.content
