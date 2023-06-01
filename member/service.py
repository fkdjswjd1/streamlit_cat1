from member.user import Member
from member.dao_db import MemberDao
import streamlit as st

class MemberService:

    loginId=''
    def login_user(self):
        if MemberService.loginId=='':
            st.write('로그인하고 이용하세요')
        else:
            a = self.dao.select(MemberService.loginId)
            st.write(a.User_Id+'님')
    def __init__(self):
        self.dao=MemberDao()
    def addMember(self,User_Id, User_Pw, User_Name, User_Email, User_Phone):
        a=Member(User_Id=User_Id,User_Pw=User_Pw,User_Name=User_Name,User_Email=User_Email,User_Phone=User_Phone)
        self.dao.insert(a)
    def getById(self,User_Id):
        a:Member=self.dao.select(User_Id=User_Id)
        if a==None:
            st.write('없는 아이디')
        else:
            st.write(a)
    def delMember(self,User_Id):
        if MemberService.loginId !='':
            st.write('로그인 하세요')
            return
        self.dao.delete(User_Id=User_Id)
    def login(self,User_Id,User_Pw):
        if MemberService.loginId!='':
            st.sidebar.write('이미 로그인중')
            return
        a=self.dao.select(User_Id=User_Id)
        if a==None:
            st.sidebar.write('없는 아이디')
            return
        else:
            if User_Pw==a.User_Pw:
                MemberService.loginId=User_Id
                st.sidebar.write('로그인 성공')
            else:
                st.sidebar.write('패스워드 불일치')

    def printMyInfo(self): #정보확인 # 로그인 상태에서만 사용가능
        if MemberService.loginId=='':
            st.write('로그인 먼저 하세요')
            return
        else:
            a=self.dao.select(MemberService.loginId)
            st.write(a)
    def logout(self):
        if MemberService.loginId=='':
            st.sidebar.write('로그인 먼저 하세요')
            return
        MemberService.loginId=''
        st.sidebar.write('로그아웃 완료!')




