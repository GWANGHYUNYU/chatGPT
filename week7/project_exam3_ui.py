# 스마트팜 환경 제어 조언 AI 어시스턴트 APP
import gradio as gr

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()

def assistant_by_current_data(
    temperature: float,
    humidity: float,
    ec: float,
    ph: float,
    co2: float,
    model: str = "gpt-5",
) -> str:
    """
    현재 센서값을 바탕으로 이상적인 스마트팜 제어환경을 자연어로 제시
    """

    SYSTEM_INSTRUCTIONS = (
        "너는 스마트팜 환경 제어 전문가다. "
        "대한민국 전라남도 곡성군 옥과면에서 스마트팜으로 레몬을 재배하고 있다. "
        "입력으로 주어진 센서값을 기반으로 현재 상태를 간단히 진단하고, "
        "현재 날짜를 기준으로 이상적인 제어 환경(온도·습도·EC·pH·CO₂ 목표 범위와 권장 제어 조치)을 3~5문장으로 설명하라. "
        "JSON이나 목록 대신 자연스러운 문장으로만 답하라."
    )

    user_text = (
        f"현재 센서값은 다음과 같습니다:\n"
        f"온도: {temperature}°C, "
        f"습도: {humidity}%, "
        f"EC: {ec} dS/m, "
        f"pH: {ph}, "
        f"CO₂: {co2} ppm.\n\n"
        "이 값을 바탕으로 이상적인 제어환경과 권장 조치를 설명해주세요."
    )

    response = client.responses.create(
        model=model,
        instructions=SYSTEM_INSTRUCTIONS,
        input=[
            {
                "role": "user",
                "content": [{"type": "input_text", "text": user_text}],
            }
        ],
    )
    return (response.output_text or "").strip()

# Gradio UI
with gr.Blocks(title="스마트팜 센서 입력 + 제어 조언") as demo:
    gr.Markdown("## 🌿 스마트팜 센서 입력 & 제어 조언 (OpenAI Responses API)")
    gr.Markdown(
        "- 슬라이더 또는 숫자 중 편한 방식으로 값을 설정하세요.\n"
        "- 환경변수를 입력한 후 **조언 받기**를 누르세요."
    )

    with gr.Row():
        model = gr.Dropdown(
            label="모델 선택",
            choices=["gpt-4o-mini", "gpt-4o", "gpt-5"],
            value="gpt-4o-mini",
        )

    with gr.Row():
        with gr.Column():
            gr.Markdown("### 🎚️ 슬라이더 입력")
            s_temp = gr.Slider(-20.0, 60.0, value=25.0, step=0.1, label="온도 (°C)")
            s_hum  = gr.Slider(0.0, 100.0, value=60.0, step=0.5, label="습도 (%)")
            s_ec   = gr.Slider(0.0, 10.0, value=1.5, step=0.01, label="EC (dS/m)")
            s_ph   = gr.Slider(0.0, 10.0, value=6.5, step=0.01, label="pH")
            s_co2  = gr.Slider(0.0, 1500.0, value=600.0, step=10.0, label="CO₂ (ppm)")
        with gr.Column():
            gr.Markdown("### 💡 스마트팜 환경 제어 조언")
            advice_out = gr.Textbox(label=" ", lines=13, show_copy_button=True)

        # --- 조언 받기 버튼 ---
    btn_advice = gr.Button("💡 조언 받기", variant="primary")

    btn_advice.click(
        fn=assistant_by_current_data,
        inputs=[s_temp, s_hum, s_ec, s_ph, s_co2, model],
        outputs=advice_out,
    )


if __name__ == "__main__":
    demo.queue().launch()