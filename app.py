# app.py
# Render 배포 연습용 앱

# 로컬 실행
# python -m streamlit run ./webservice/day31/myapp/app.py

# Render Cloud 실행
# streamlit irn app.py --server.address 0.0.0.0 --server.port $PORT
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

DEFAULT_GREETING = '안녕하세요'
APP_GREETING = os.getenv('APP_GREETING', DEFAULT_GREETING)
#////
st.set_page_config(
    page_title='Render배포 연습 앱v2',
    page_icon= '🚖',
    layout='centered',
)

st.title('✈ Render 배포 연습 앱V2')
st.write('이 화면이 보이면 앱이 정상적으로 실행되고 있다는 것입니다.')

st.divider()

st.subheader('간단한 인사말 만들기')

name = st.text_input('이름을 입력해 주세요.',placeholder='예) 홍길동')

if st.button('인사말 확인',type='primary'):
    if name.strip():
        st.success(f'{APP_GREETING},{name.strip()}님! Render 배포가 잘 되었습니다!')
    else:
        st.warning('이름을 먼저 입력해 주세요!')

st.divider()

st.subheader('환경변수 설정 확인')

if os.getenv('APP_GREETING'):
    st.success('APP_GREETING 환경변수를 성공적으로 읽었습니다!')
    st.write(f'현재 인사말 설정 값: {APP_GREETING}')
else:
    st.info(f'APP_GREETING 환경변수가 설정되지 않아 기본값을 사용 중입니다!')

















































