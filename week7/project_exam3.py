# 스마트팜 환경 제어 조언 AI 어시스턴트
import random

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()


def generate_sensor_data():
    """랜덤한 센서값 1세트를 생성"""
    data = {
        "temperature": round(random.uniform(15.0, 35.0), 2),  # °C
        "humidity": round(random.uniform(30.0, 90.0), 2),     # %
        "co2": round(random.uniform(400.0, 1000.0), 2),       # ppm
        "ec": round(random.uniform(0.5, 3.0), 2),             # dS/m (전기전도도)
        "ph": round(random.uniform(5.5, 7.5), 2)              # pH
    }
    return data

def assistant_by_current_data(data: dict, model: str = "gpt-5") -> str:
    """
    현재 센서값(data)을 바탕으로, 이상적인 스마트팜 제어환경을 자연어 문장으로 제시.
    출력 예시:
    "현재 온도는 29.4°C로 다소 높습니다. 온도를 25°C 근처로 낮추기 위해 환기팬을 작동하는 것이 좋습니다..."
    """
    SYSTEM_INSTRUCTIONS = (
        "너는 스마트팜 환경 제어 전문가다. "
        "대한민국 전라남도 전라남도 곡성 옥과면에서 스마트팜으로 레몬을 재배하고 있다. "
        "입력으로 주어진 센서값을 기반으로 현재 상태를 간단히 진단하고, "
        "현재 날짜를 기준으로 이상적인 제어 환경(온도·습도·EC·pH·CO2 목표 범위와 권장 제어 조치)을 3~5문장으로 설명하라. "
        "JSON이나 목록 대신 자연스러운 문장으로만 답하라."
    )

    # 입력 텍스트 구성
    user_text = (
        f"현재 센서값은 다음과 같습니다:\n"
        f"온도: {data.get('temperature', 'N/A')}°C, "
        f"습도: {data.get('humidity', 'N/A')}%, "
        f"EC: {data.get('ec', 'N/A')} dS/m, "
        f"pH: {data.get('ph', 'N/A')}, "
        f"CO₂: {data.get('co2', 'N/A')} ppm.\n\n"
        "이 값을 바탕으로 이상적인 제어환경과 권장 조치를 설명해주세요."
    )

    response = client.responses.create(
        model=model,
        instructions=SYSTEM_INSTRUCTIONS,
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": user_text}
                ]
            }
        ]
    )

    return (response.output_text or "").strip()

if __name__ == "__main__":
    sensor_data = generate_sensor_data()
    print("=== 스마트팜 장소: 전라남도 곡성 옥과면 ===")
    print("=== 스마트팜 작목: 레몬 ===")
    print(sensor_data)

    advice = assistant_by_current_data(sensor_data, model="gpt-5")
    print("\n=== 스마트팜 환경 제어 조언 ===")
    print(advice)