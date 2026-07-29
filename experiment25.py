from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Write a short paragraph about Artificial Intelligence."
)

print(response.output_text)