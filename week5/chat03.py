from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

# Role: 역할
# system - 음악을 좋아하는 사람, 음식을 잘하는 사람, 코딩 전문가, 조언 전문가, ...
# assistant - 챗봇
# user - 사용자

# response = client.responses.create(
#     model="gpt-4o-mini",
#     input=[
#         # {
#         #     "role": "system",
#         #     "content": "당신은 프로그래밍 전문가입니다. 사용자가 입력한 분야에 필요한 기술과 학습 방법을 3문장 이내로 알려주세요."
#         # },
#         {
#             "role": "user",
#             "content": "보안 전문가"
#         }
#     ]
# )

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "system",
            "content": "당신은 프로그래밍 학습 조언가입니다."
        },
        {
            "role": "user",
            "content": "초보자가 배우기 좋은 언어를 하나 추천해줘. 이름만 알려줘."
        },
        {
            "role": "assistant",
            # "content": "파이썬(Python)"
            "content": "코틀린(Kotlin)"
        },
        {
            "role": "user",
            "content": "어떤 분야에 활용할 수 있어? 간단히 설명해줘."
        }
    ]
)

print(response.output_text)