import datetime
from PIL import Image
import streamlit as st

def write_life_page():
    st.subheader('하루 기록 서비스 📝')
    breakfast_food = 20
    lunch_food = 20
    dinner_food = 15
    breakfast_water = 50
    lunch_water = 10
    dinner_water = 25
    weight = 15.5
    playtime = 2
    check1 = 1
    check2 = 0
    check3 = 1
    check4 = 0
    check5 = 0
    check6 = 1
    check7 = 0
    check8 = 0
    check9 = 0
    check10 = 1
    memo="밥먹다가 뒤로 넘어짐. 혼자 숨바꼭질함."

# 꾸미기
#     font_css = """
#     <style>
#     button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
#       font-size: 24px;
#     }
#     </style>
#     """
#
#     st.write(font_css, unsafe_allow_html=True)
    font_css = """
    <style>
    button[data-baseweb="tab"]   {
      background: #EAEAEA55;
    }
    </style>
    """

    st.write(font_css, unsafe_allow_html=True)

    listtabs=["일지 보기","오늘의 일지 작성","보고서"]
    whitespace = 15

    tabs = st.tabs([s.center(whitespace, "\u2001") for s in listtabs])
    # tab1, tab2, tab3 = st.tabs(["  일지 보기  ","  오늘의 일지 작성  ","  보고서  "])
    with tabs[0]:
        col1,col2=st.columns([1,2],gap='large')
        with col1:
            now = datetime.datetime.now()
            year=int(now.strftime('%Y'))
            month = int(now.strftime('%m'))
            day = int(now.strftime('%d'))
            st.markdown('###### 👇날짜 선택')
            choose_date=st.date_input('👇날짜 선택',datetime.date(year,month,day),label_visibility='collapsed')
        with col2:
            st.markdown('###### 👇기록 확인')

            with st.expander(f'{choose_date}의 기록'):
            # st.write(f'{choose_date}의 기록')

                subcol13,subcol14,subcol15=st.columns([1,1,3])
                subcol13.markdown('###### ▪️ 몸무게')
                kilogram='kg'
                subcol14.text_input('몸무게',value=str(weight) + kilogram, disabled=True,label_visibility='collapsed')

                subcol13,subcol14,subcol15=st.columns([1,1,3])
                subcol13.markdown('###### ▪️ 놀이시간')
                hour='hour'
                subcol14.text_input('놀이시간',value=str(playtime) + hour, disabled=True,label_visibility='collapsed')


                st.markdown('###### ▪️ 사료급여량')
                gram='gram'
                subcol1,subcol2,subcol3,subcol4,subcol5,subcol6=st.columns([1,2,1,2,1,2],gap='medium')
                subcol1.write('아침')
                subcol2.text_input('아침사료량',value=str(breakfast_food) + gram, disabled=True,label_visibility='collapsed')
                subcol3.write('점심')
                subcol4.text_input('점심사료량',value=str(lunch_food) + gram, disabled=True,label_visibility='collapsed')
                subcol5.write('저녁')
                subcol6.text_input('저녁사료량',value=str(dinner_food) + gram, disabled=True,label_visibility='collapsed')

                st.markdown('###### ▪️ 음수량')
                ml = 'ml'
                subcol1,subcol2,subcol3,subcol4,subcol5,subcol6= st.columns([1, 2, 1, 2, 1, 2], gap='medium')
                subcol1.write('아침')
                subcol2.text_input('아침음수량', value=str(breakfast_water) + ml, disabled=True, label_visibility='collapsed')
                subcol3.write('점심')
                subcol4.text_input('점심음수량', value=str(lunch_water) + ml, disabled=True, label_visibility='collapsed')
                subcol5.write('저녁')
                subcol6.text_input('저녁음수량', value=str(dinner_water) + ml, disabled=True, label_visibility='collapsed')
                c_col1,c_col2,c_col3,c_col4,c_col5=st.columns(5)
                c_col1.checkbox(label=":drop_of_blood:",value=bool(check1),disabled=True)
                c_col2.checkbox(label="🪫", value=bool(check2), disabled=True)
                c_col3.checkbox(label="💊", value=bool(check3), disabled=True)
                c_col4.checkbox(label="🌡", value=bool(check4), disabled=True)
                c_col5.checkbox(label="🛁", value=bool(check5), disabled=True)
                st.write("")
                c_col1, c_col2, c_col3, c_col4, c_col5 = st.columns(5)
                c_col1.checkbox(label="👂", value=bool(check6), disabled=True)
                c_col2.checkbox(label="😿", value=bool(check7), disabled=True)
                c_col3.checkbox(label="😺", value=bool(check8), disabled=True)
                c_col4.checkbox(label="😸", value=bool(check9), disabled=True)
                c_col5.checkbox(label="😻", value=bool(check10), disabled=True)
                st.markdown('###### ▪️ 메모')
                st.text_area('memo',value=memo,disabled=True, label_visibility="collapsed")
    with tabs[1]:
        st.write('오늘의 일지 작성')

    with tabs[2]:
        st.write("")
        st.write("")
        st.subheader('통계보기 📊')
        col1,col2,col3=st.columns([1,1,2])
        col1.selectbox("기간",("1주일","1개월","6개월","1년"),label_visibility="collapsed")

    # 데이터베이스 연동 후 그래프


