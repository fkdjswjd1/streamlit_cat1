
import streamlit as st
from streamlit_option_menu import option_menu
import Diagnosing_eye
import signup
import AI_Chatbot
import Write_life
import About

st.title('냥이의 하루, 안냥:cat:')
menu = ["About", "Diagnosing eye", "AI Chatbot","Write life","Signup"]
with st.sidebar:
    choose = option_menu("Menu",menu,
                         icons=['house', 'camera fill', 'bi-chat-dots','bi-clipboard-check', 'kanban'],
                         menu_icon="bi-balloon-fill", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

def main():
    if choose == menu[0]:
        About.About_page()
    if choose == menu[1]:
        Diagnosing_eye.diagnosing_eye_page()
    if choose == menu[2]:
        AI_Chatbot.AI_Chatbot_page()
    if choose == menu[3]:
        Write_life.write_life_page()
    if choose == menu[4]:
        signup.signup_page()

# User 테이블 생성 : 한번만 실행
import sqlite3
# con=sqlite3.connect('database.db')
# cur=con.execute("""
# create table User(
# User_Id char(15) primary key,
# User_Pw char(20),
# User_Name char(45),
# User_Email char(100),
# User_Phone char(20))
# """)
# cur.close()
# con.close()

main()

def login_user(id, pwd): # 로그인을 위한 함수
    con = sqlite3.connect('database.db')
    cur=con.execute(f"SELECT * FROM User WHERE User_Id = '{id}' and User_Pw = '{pwd}'")
    return cur.fetchone()





st.sidebar.write('로그인')

login_id = st.sidebar.text_input('아이디', placeholder='아이디를 입력하세요')
login_pw = st.sidebar.text_input('패스워드',
                                 placeholder='패스워드를 입력하세요',
                                 type='password')

login_btn = st.sidebar.button('로그인')

if login_btn:
    user_info = login_user(login_id, login_pw)
    if user_info:
        st.sidebar.write(user_info[2]+'님, 안녕하세요:smile:')
    else:
        st.sidebar.write('로그인에 실패했습니다.')



