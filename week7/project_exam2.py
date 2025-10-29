# 문장 3줄 요약 챗봇
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

user_input = input("3줄 요약을 위한 문장을 입력하세요: ")

SYSTEM_INSTRUCTIONS = (
    "너는 전문 요약가다. 출력은 반드시 정확히 3줄로만 작성하라. "
    "핵심 사실(누가/무엇/언제·어디서/왜·어떻게)을 간결하게 담고, 불필요한 수식어는 줄여라."
)

response = client.responses.create(
    model="gpt-5",
    instructions=SYSTEM_INSTRUCTIONS,
    input=[
        {
            "role": "user",
            "content": [
                    {
                        "type": "input_text",
                        "text": f"다음 텍스트를 정확히 3줄로 요약해줘:\n\n{user_input}"
                    }
                ]
            }
        ]
    )

summary = (response.output_text or "").strip()

print("\n3줄 요약 결과: ", summary)
print("\n=== 3줄 요약 챗봇이 종료되었습니다 ===")