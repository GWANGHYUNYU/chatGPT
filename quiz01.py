# 별자리 챗봇
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

user_input = input("생일을 입력하세요: ")

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "user",
            "content": f"사용자가 입력한 생일 {user_input}에 해당하는 별자리를 알려주고, 그 별자리 사람들의 특징과 성격을 3문장 이내로 알려줘."
        }
    ]
)

print("챗봇: ", response.output_text)

# messages = [
#     {"role": "system", "content": "당신은 별자리 전문가입니다. 사용자가 생일을 입력하면 해당 별자리와 그 성격 및 특징을 3문장 이내로 설명해 주세요."}
# ]

# while True:
#     user_input = input("생일을 입력하세요: ")
#     if user_input.lower() in ["quit", "exit", "bye"]:
#         print("챗봇을 종료합니다.")
#         break

#     messages.append(
#         {"role": "user", "content": user_input}
#     )

#     response = client.responses.create(
#         model="gpt-4o-mini",
#         input=messages
#     )

#     result = response.output_text
#     print("챗봇:", result)
#     print("ChatGPT 응답 완료")

#     break

#     messages.append(
#         {"role": "assistant", "content": result}
#     )