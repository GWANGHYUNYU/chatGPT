# 초간단 MBTI 테스트
import json

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

def generate_mbti_question():
    prompt = """
다음 지시에 따라 반드시 JSON만 출력해.
MBTI 성격 유형을 판별할 수 있는 객관식 질문 4개를 JSON 형식으로 만들어줘.
각 질문은 다음 MBTI 요소를 순서대로 판별해야 해.
1. 외향형(E) vs 내향형(I)
2. 감각형(S) vs 직관형(N)
3. 사고형(T) vs 감정형(F)
4. 판단형(J) vs 인식형(P)

출력은 아래 예시와 같은 JSON 객체만 출력할 것. 
설명이나 추가 텍스트는 절대 넣지 마.

{
    "questions": [
        {
            "question": "새로운 사람을 만났을 때 나는?",
            "options": {
                "a": "먼저 말을 걸고 대화를 주도한다.",
                "b": "상대가 말을 걸어오면 대화한다."
            },
            "types": {
                "a": "E",
                "b": "I"
            }
        }
    ]
}
"""

# 질문지
# a) 첫번째 보기 = E
# b) 두번째 보기 = I

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        # response_format={"type": "json_object"}
    )

    return response.output_text

def take_mbti_test(questions):
    questions = json.loads(questions)
    # print(questions)
    mbti = ""

    for item in questions["questions"]:
        print(f"질문: {item['question']}")
        print(f"a) {item['options']['a']}")
        print(f"b) {item['options']['b']}")
        print()
        answer = input("답변을 선택하세요 (a 또는 b): ").strip().lower()
        while answer not in ['a', 'b']:
            answer = input("답변을 선택하세요 (a 또는 b): ").strip().lower()
        if answer in item["types"]:
            mbti += item["types"][answer]

        print()
        print("-" * 40)
    
    return mbti

def mbti_analysis(mbti_type):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "user",
                "content": f"MBTI 유형 {mbti_type}의 성격 유형의 특징을 3문장 이내로 간단히 설명해줘."
            }
        ]
    )

    return response.output_text

print("=== 초간단 MBTI 테스트 ===\n")

# MBTI 질문지 생성
questions = generate_mbti_question()
# print("생성된 질문지:", questions)

# 사용자가 질문지를 직접 풀이
mbti_type = take_mbti_test(questions)
print(f"당신의 MBTI 유형은 {mbti_type}입니다!")

# 성격 유형 분석
result = mbti_analysis(mbti_type)
print(result)
print("\n=== 테스트가 종료되었습니다 ===")