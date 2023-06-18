# main.py

import streamlit as st
import requests

# 사용자로부터 데이터 값을 입력받습니다.
data_value = st.number_input("데이터 값 입력", value=0.0)

# 데이터 값을 Flask API로 전송합니다.
response = requests.post('http://localhost:5000/api/data', json={'data_value': data_value})

# API 응답을 확인하고 시각화합니다.
if response.status_code == 200:
    st.image(response.content)
else:
    st.error(f"API 요청이 실패하였습니다. 상태 코드: {response.status_code}")


