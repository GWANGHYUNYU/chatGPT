from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("사용자 입력: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("챗봇을 종료합니다.")
        break

    messages.append(
        {"role": "user", "content": user_input}
    )

    response = client.responses.create(
        model="gpt-4o-mini",
        input=messages
    )

    result = response.output_text
    print("챗봇:", result)

    messages.append(
        {"role": "assistant", "content": result}
    )