import streamlit as st
import sqlite3

def signup_user(input_id,input_pwd,input_name,input_email,input_phone):
    st.write(input_id)
    con=sqlite3.connect('database.db')
    cur=con.cursor()

    cur.execute(f"insert into User (User_Id, User_Pw, User_Name, User_Email, User_Phone) VALUES ("+
                f"'{input_id}', '{input_pwd}', '{input_name}','{input_email}', '{input_phone}')")
    con.commit()
    cur.close()
    con.close()

def signup_page():
    global check1
    st.subheader('회원가입')
    st.info('다음 양식을 모두 입력 후 제출합니다.')
    input_id = st.text_input('아이디', max_chars=15)
    input_pwd = st.text_input('비밀번호', type='password')
    input_pwd2 = st.text_input('비밀번호 확인', type='password')
    checkbtn = st.button('확인')
    if checkbtn:
        if input_pwd != input_pwd2:
            st.error('비밀번호가 다릅니다. 다시 입력해주세요', icon="🚨")
            check1 = 0
        elif input_pwd=='':
            st.error('비밀번호를 입력하세요', icon="🚨")
            check1=0
        else:
            st.success('확인되었습니다.', icon="✅")
            check1=1
    input_name = st.text_input('닉네임', max_chars=45)
    input_email = st.text_input('이메일', max_chars=100)
    input_phone = st.text_input('전화버호', max_chars=20)

    submitted=st.button('회원가입하기')
    if submitted:
        if check1==1:
            signup_user(input_id,input_pwd,input_name,input_email,input_phone)
            st.success(f'{input_id}님,환영합니다! 로그인해주세요.', icon="✅")
        elif check1==0:
            st.error('비밀번호 확인버튼을 클릭해주세요', icon="🚨")
        else:
            st.write('error')






        # if submitted:
        #     st.success('환영합니다!', icon="✅")
        #     con=sqlite3.connect('database.db')
        #     cur=con.cursor()
        #
        #     cur.execute(f"INSERT INTO User(User_Id, User_Pw, User_Name, User_Email, User_Phone) VALUES ("
        #                 f"'{input_id}', '{input_pwd}', '{input_name}','{input_email}', '{input_phone}')")
        #     con.commit()
        #     cur.close()
        #     con.close()
