from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

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