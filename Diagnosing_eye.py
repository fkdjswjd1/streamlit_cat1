import os.path
from PIL import Image
import streamlit as st

def load_image(image_file):
    img=Image.open(image_file)
    return img

def diagnosing_eye_page():
    col1, col2=st.columns([3,2])
    with col1:
        st.subheader('안구질환 진단:eye:')
        st.markdown('''
        고양이의 안구질환은 조기에 치료하지 않으면 큰 질병까지 이어질 수 있습니다.
      그러니 이 서비스를 이용하여 주기적으로 진단받으세요.
      
      ###### [서비스 이용방법]
      1. 고양이의 눈만 보이도록 사진을 찍습니다.
      2. 사진을 업로드하고 결과보기를 버튼을 클릭합니다.
      3. 결과와 질환에 대한 통계를 확인합니다.
      
      + AI챗봇에 질환에 대해 물어보면 더 많은 정보를 얻을 수 있습니다.
        ''')

    uploaded_file=st.file_uploader('사진 업로드 해주세요',type=['jpg'])


    with col2:
        st.markdown('###### 업로그 사진 보기')
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image.', width=300)
