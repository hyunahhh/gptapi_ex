from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# 환경변수 생성
gpt_api_key = os.environ.get('OPEN_API_key')


# api 연결
client = OpenAI(
    # api_key="gpt api key 넣기"
    api_key=gpt_api_key)
    
# print("인증성공")
messages = []

# gpt 모델에 질문을 보냄

while True:
    content = input("사용자: ")

    if content.lower() == 'q':
        print("대화를 종료합니다.")
        break

    messages.append({"role": "user", "content": content})

    complation = client.chat.completions.create(
        # model = "gpt-3.5-turbo",
        model = "gpt-4-turbo",
        messages = messages
    )

    chat_response = complation.choices[0].message.content
    print(f"ChatGPT : {chat_response}")
    messages.append({"role": "assistant", "content": chat_response})


