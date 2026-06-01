from openai import OpenAI

client = OpenAI(api_key="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")


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello"}]
)

print(response.choices[0].message.content)