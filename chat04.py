from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

# response = client.responses.create(
#     model="gpt-4o-mini",
#     input=[
#         {
#             "role": "system",
#             "content": "뉴스 제목을 보고 어떤 카테고리에 속하는지 알려줘."
#         },
#         {
#             "role": "user",
#             "content": "새로운 블랙홀 발견, 우주 연구에 새로운 가능성"
#         }
#     ]
# )

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "system",
            "content": "뉴스 제목을 보고 어떤 카테고리에 속하는지 알려줘."
        },
        {
            "role": "user",
            "content": "챔피언스 리그, 치열한 순위 다툼"
        },
        {
            "role": "assistant",
            "content": "스포츠"
        },
        {
            "role": "user",
            "content": "자율주행 자동차, 내년부터 상용화 추진"
        },
        {
            "role": "assistant",
            "content": "기술"
        },
        {
            "role": "user",
            "content": "새로운 블랙홀 발견, 우주 연구에 새로운 가능성"
        }
    ]
)

print(response.output_text)