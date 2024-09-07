import streamlit as st
from openai import OpenAI
import os

# OpenAI 클라이언트 초기화
openai_api_key = st.secrets["openai"]["api_key"]
client = OpenAI(api_key  = openai_api_key)

# 이미지 사이즈와 장 수 선택 메뉴 추가  
size_options = ["640x480", "800x600", "1024x768"]  
num_images_options = [1, 2]  

# 사용자 입력을 위한 프롬프트  
prompt = st.text_input("이미지 생성을 위한 프롬프트를 입력하세요:")  

# 이미지 사이즈 선택  
selected_size = st.selectbox("이미지 사이즈를 선택하세요:", size_options)  

# 이미지 장 수 선택  
selected_num_images = st.selectbox("생성할 이미지 장 수를 선택하세요:", num_images_options)  

if st.button("이미지 생성"):  
    if prompt:  
        try:  
            kwargs = {  
                "prompt": prompt,  
                "n": selected_num_images,  # 선택한 이미지 장 수  
                "size": selected_size  # 선택한 이미지 사이즈  
            }  

            # OpenAI API를 사용하여 이미지 생성  
            response = client.images.generate(**kwargs)  

            # 생성된 이미지 표시  
            for i in range(selected_num_images):  
                image_url = response.data[i].url  
                st.image(image_url, caption=f"생성된 이미지 {i + 1}", use_column_width=True)  

        except Exception as e:  
            st.error(f"이미지 생성 중 오류 발생: {e}")  
    else:  
        st.warning("이미지를 생성하려면 프롬프트를 입력하세요.")
