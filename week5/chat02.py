from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "user",
            "content": "코딩을 배워야 하는 이유를 2문장으로 설명해줘"
        }
    ],
    # temperature=1.5  # 0~2, 높을수록 창의적
    max_output_tokens=20    # 출력 토큰 수 제한
)

print(response.output_text)
