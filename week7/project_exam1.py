# 혈액형 성격 요약 챗봇
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

user_input = input("혈액형을 입력하세요(예시: A형, B형, AB형, O형): ")

response = client.responses.create(
    model="gpt-5",
    input=[
        {
            "role": "user",
            "content": f"사용자가 입력한 혈액형 {user_input}에 해당하는 사람들의 특징과 성격을 3문장 이내로 알려줘."
        }
    ]
)

print("\n챗봇: ", response.output_text)
print("\n=== 혈액형 성격 챗봇이 종료되었습니다 ===")