import streamlit as st
from openai import OpenAI
import os
import time

# OpenAI 클라이언트 초기화
openai_api_key = st.secrets["openai"]["api_key"]
client = OpenAI(api_key=openai_api_key)

# Streamlit 앱 레이아웃
st.title("AI 이미지 생성기")
st.write("텍스트 프롬프트를 입력하고 AI 이미지를 생성하세요.")

# 텍스트 입력
prompt = st.text_input("프롬프트를 입력하세요:")

# 이미지 사이즈 선택
size = st.selectbox("이미지 사이즈를 선택하세요:", ["256x256", "512x512", "1024x1024"])

# 이미지 장수 선택
num_images = st.slider("이미지 장수를 선택하세요:", 1, 5, 1)

if st.button("이미지 생성"):
    if prompt:
        try:
            kwargs = {
                "prompt": prompt,
                "n": num_images,
                "size": size
            }

            # OpenAI API를 사용하여 이미지 생성
            response = client.images.generate(**kwargs)

            # 응답에서 이미지 URL 추출 및 표시
            for i, data in enumerate(response.data):
                image_url = data.url
                st.image(image_url, caption=f"생성된 이미지 {i+1}", use_column_width=True)

        except Exception as e:
            if 'rate_limit_exceeded' in str(e):
                st.error("요청 한도를 초과했습니다. 잠시 후 다시 시도하세요.")
                time.sleep(60)  # 1분 대기
            else:
                st.error(f"이미지 생성 중 오류 발생: {e}")
    else:
        st.warning("이미지를 생성하려면 프롬프트를 입력하세요.")
