import streamlit as st
from member.service import MemberService


class login_page:
    def __init__(self):
        self.service=MemberService()
    def run(self):
        login_id = st.sidebar.text_input('아이디', placeholder='아이디를 입력하세요')
        login_pw = st.sidebar.text_input('패스워드',
                                         placeholder='패스워드를 입력하세요',
                                         type='password')
        login_btn = st.sidebar.button('로그인하기')
        if login_btn:

            self.service.login(login_id, login_pw)



if __name__ == '__main__':
    m = login_page()
    m.run()