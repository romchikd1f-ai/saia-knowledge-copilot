import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

model = os.getenv(
    "OPENAI_MODEL",
    "gpt-6-astra"
)

response = client.responses.create(
    model=model,
    input="Объясни RAG 12-летнему ребёнку в 3 предложениях."
)

print(response.output_text)
print(response.id)
print(response.model)
print(response.usage)