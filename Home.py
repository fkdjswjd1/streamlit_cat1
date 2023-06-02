import streamlit as st
from streamlit_option_menu import option_menu
import Diagnosing_eye
from member.service import MemberService
from signup import signup_page
from login import login_page
from logout import logout_page
from Mypage import Mypage_page
import AI_Chatbot
import Write_life
import About



class Home:
    def __init__(self):
        self.signup=signup_page()
        self.login=login_page()
        self.logout=logout_page()
        self.service=MemberService()
        self.Mypage = Mypage_page()
    def run(self):
        st.set_page_config(
            page_title='냥이의 하루, 안냥 ',
            page_icon=':cat:',
            layout='wide',  # wide,centered
            menu_items={
                'Get Help': 'https://lc.multicampus.com/k-digital/#/login',  # 페이지로 이동하기
                'About': '### 대박징조의 *반려묘의 안구질환 진단 및 하루 기록 서비스* 입니다.'
            },
            initial_sidebar_state='expanded'
        )

        st.title('냥이의 하루, 안냥:cat:')
        if self.service.login_user(print=False) == '':
            login_logout='login'
        else:
            login_logout='logout'
        menu = ["About", "Signup",login_logout,"Mypage","Diagnosing eye", "AI Chatbot","Write life"]
        with st.sidebar:
            choose = option_menu("Menu",menu,
                                 icons=['house', 'bi-clipboard-check','person lines fill','gear','camera fill', 'bi-chat-dots','book'],
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
                self.signup.run()
            if choose == menu[2]:
                self.login.run()
            if choose == menu[3]:
                self.Mypage.run()
            if choose == menu[4]:
                Diagnosing_eye.diagnosing_eye_page()
            if choose == menu[5]:
                AI_Chatbot.AI_Chatbot_page()
            if choose == menu[6]:
                Write_life.write_life_page()





        self.service.login_user()
        st.markdown("---")
        main()




if __name__== '__main__':
    m=Home()
    m.run()
