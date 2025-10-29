# 문장 3줄 요약 Gradio 앱
import re
import gradio as gr

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

SYSTEM_INSTRUCTIONS = (
    "너는 전문 요약가다. 출력은 반드시 정확히 3줄로만 작성하라. "
    "핵심 사실(누가/무엇/언제·어디서/왜·어떻게)을 간결하게 담고, 불필요한 수식어는 줄여라."
    "3줄의 각 문장은 마침표로 끝나야 한다."
    "각 문장 수는 한글 기준 10~20단어 이내로 작성하라."
)

def summarize_to_3_lines(text: str, model: str = "gpt-5") -> str:
    if not text or not text.strip():
        return "에러: 요약할 문장을 입력하세요."
    response = client.responses.create(
        model=model,
        instructions=SYSTEM_INSTRUCTIONS,
        input=[
            {
                "role": "user",
                "content": [
                        {
                            "type": "input_text",
                            "text": f"다음 텍스트를 정확히 3줄로 요약해줘:\n\n{text}"
                        }
                    ]
                }
            ]
        )
    return (response.output_text or "").strip()

with gr.Blocks(title="문장 3줄 요약기") as demo:
    gr.Markdown("## ✂️ 문장 3줄 요약기 (OpenAI Responses API)")
    gr.Markdown("- 아래 입력창에 긴 문장을 붙여넣고 **요약하기**를 누르세요.\n- 결과는 정확히 3줄로 출력됩니다.")
    with gr.Row():
        with gr.Column():
            inp = gr.Textbox(
                label="요약할 문장",
                placeholder="여기에 요약하고 싶은 문장을 붙여넣으세요.",
                lines=8
            )
            model = gr.Dropdown(
                label="모델 선택",
                choices=["gpt-4o-mini", "gpt-4o", "gpt-5"],
                value="gpt-5"
            )
            btn = gr.Button("요약하기", variant="primary")
        with gr.Column():
            out = gr.Textbox(label="3줄 요약 결과", lines=6, show_copy_button=True)

    btn.click(fn=summarize_to_3_lines, inputs=[inp, model], outputs=out)

if __name__ == "__main__":
    demo.queue().launch()