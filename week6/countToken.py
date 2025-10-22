import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o-mini")

text = "코딩을 배우면 문제 해결 능력을 키울 수 있으며, 현대 사회에서 필수적인"
tokens = enc.encode(text)

print("토큰 개수:", len(tokens))
print("토큰 IDs:", tokens)
