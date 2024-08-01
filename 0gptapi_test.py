from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


gpt_api_key = os.environ.get('OPEN_API_key')

client = OpenAI(
    # api_key="gpt api key 넣기"
    api_key=gpt_api_key)
    
# print("인증성공")

# gpt 모델에 질문을 보냄
response = client.chat.completions.create(
    model="gpt-3.5-turbo" ,
    messages=[
        #{"role":"system", "content" :"너는 IT전문가야"},
        {"role":"user", "content" :"전세계에서 가장 많이 쓰는 언어 TOP5를 이야기해줘"}
    ]
)

print(response.choices[0].message.content)
