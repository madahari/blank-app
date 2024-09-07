import streamlit as st
from openai import OpenAI
import os

# OpenAI 클라이언트 초기화
openai_api_key = st.secrets["openai"]["api_key"]
client = OpenAI(api_key=openai_api_key)

# Streamlit 앱 레이아웃
st.title("AI 이미지 생성기")
st.write("텍스트 프롬프트를 입력하고 AI 이미지를 생성하세요.")

# 텍스트 입력
prompt = st.text_input("프롬프트를 입력하세요:")

# 이미지 스타일 선택
style_options = [
    "사실적인",
    "만화 스타일",
    "수채화",
    "유화",
    "팝아트",
    "추상화",
    "미니멀리즘",
    "3D 렌더링"
]
selected_style = st.selectbox("이미지 스타일을 선택하세요:", style_options)

if st.button("이미지 생성"):
    if prompt:
        try:
            # 선택된 스타일을 프롬프트에 추가
            full_prompt = f"{prompt}, {selected_style} 스타일"
            
            kwargs = {
                "prompt": full_prompt,
                "n": 1,
                "size": "1024x1024"
            }

            # OpenAI API를 사용하여 이미지 생성
            response = client.images.generate(**kwargs)

            # 응답에서 이미지 URL 추출
            image_url = response.data[0].url

            # 생성된 이미지 표시
            st.image(image_url, caption=f"생성된 이미지 ({selected_style} 스타일)", use_column_width=True)

        except Exception as e:
            st.error(f"이미지 생성 중 오류 발생: {e}")
    else:
        st.warning("이미지를 생성하려면 프롬프트를 입력하세요.")
