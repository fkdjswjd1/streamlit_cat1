from pet.cat import Pet
from pet.pet_db import PetDao
from member.service import MemberService
import streamlit as st

class PetService:
    loginId = ''
    def __init__(self):
        self.dao=PetDao()
        self.service = MemberService()
    def addCat(self,User_Id,Cat_Name,Cat_Age,Cat_Num,Cat_Kind,Cat_Gender):
        a=Pet(User_Id=User_Id,Cat_Name=Cat_Name,Cat_Age=Cat_Age,Cat_Num=Cat_Num,Cat_Kind=Cat_Kind,Cat_Gender=Cat_Gender)
        self.dao.insert(a)

    def printCatInfo(self,User_Id):
        self.dao.select(User_Id)

    def delCat(self,User_Id):
        if MemberService.loginId !='':
            self.dao.delete(User_Id=User_Id)
            MemberService.loginId = ''
        else:
            st.write('등록된 고양이가 없습니다')
            return
