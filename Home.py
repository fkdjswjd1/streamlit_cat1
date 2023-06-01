import streamlit as st
from streamlit_option_menu import option_menu
import Diagnosing_eye
from member.service import MemberService
from signup import signup_page
from login import login_page
from logout import logout_page
import AI_Chatbot
import Write_life
import About



class Home:
    def __init__(self):
        self.signup=signup_page()
        self.login=login_page()
        self.logout=logout_page()
        self.service=MemberService()
    def run(self):
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
                self.signup.run()

        self.service.login_user()
        st.markdown("---")
        main()
        self.login.run()
        self.logout.run()



if __name__== '__main__':
    m=Home()
    m.run()
