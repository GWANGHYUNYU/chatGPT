from openai import OpenAI
client = OpenAI(api_key="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")

response = client.responses.create(
    model="gpt-5",
    input=[
        {
            "role": "user",
            "content": "너는 누구야?"
        }
    ]
)

# print(response)
print(response.output_text)