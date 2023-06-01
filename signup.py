import streamlit as st
import sqlite3


def signup_page():
    st.subheader('회원가입')
    with st.form('my_form', clear_on_submit=True):
        st.info('다음 양식을 모두 입력 후 제출합니다.')
        input_id = st.text_input('아이디', max_chars=15,)
        input_pwd = st.text_input('비밀번호',type='password')
        input_pwd2= st.text_input('비밀번호 확인',type='password')
        input_name = st.text_input('닉네임', max_chars=45)
        input_email = st.text_input('이메일', max_chars=100)
        input_phone = st.text_input('전화버호',max_chars=20)


        submitted = st.form_submit_button('제출')
        if submitted:
            con=sqlite3.connect('database.db')
            cur=con.cursor()

            cur.execute(f"INSERT INTO User(User_Id, User_Pw, User_Name, User_Email, User_Phone) VALUES ("
                        f"'{input_id}', '{input_pwd}', '{input_name}','{input_email}', '{input_phone}')")
            con.commit()
            cur.close()
            con.close()
