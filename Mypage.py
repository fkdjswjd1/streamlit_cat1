import streamlit as st
from member.service import MemberService
from member.dao_db import MemberDao
from pet.petsv import PetService
from pet.pet_db import PetDao
import sqlite3
class Mypage_page:
    def __init__(self):
        self.service=MemberService()
        self.petsv=PetService()
    def run(self):
        tab1, tab2, tab3 = st.tabs(['회원정보', '반려묘등록', '반려묘정보'])
        with tab1:
            st.subheader('회원정보 탈퇴')
            if st.button('탈퇴'):
                self.service.delMember(MemberService.loginId)
            st.subheader('회원정보 수정')
            input_name = st.text_input('닉네임', max_chars=45)
            input_email = st.text_input('이메일', max_chars=100)
            input_phone = st.text_input('전화번호', max_chars=20)
            submitted = st.button('수정')
            if submitted:
                con = sqlite3.connect('mydb.db')
                cur = con.cursor()
                sql = 'update User set User_Name=?, User_Email=?, User_Phone=? where User_Id=?'
                d = (input_name,input_email,input_phone,MemberService.loginId)
                cur.execute(sql,d)
                con.commit()
                cur.close()
                con.close()
                return st.write('수정 완료되었습니다.')


        with tab2:
            st.subheader('반려묘 등록')
            st.info('다음 양식을 모두 입력 후 제출합니다.')
            input_Name = st.text_input('반려묘이름', max_chars=45)
            input_Age = st.number_input('반려묘나이', value=1, min_value=1, step=1)
            input_Num = st.text_input('반려묘등록번호', max_chars=20)
            input_Kind = st.text_input('반려묘종', max_chars=20)
            input_Gender = st.text_input('반려묘성별', max_chars=5)
            submitted = st.button('반려묘 등록하기')
            if submitted:
                if MemberService.loginId == '':
                    st.write('로그인하고 이용하세요')
                else:
                    self.petsv.addCat(MemberService.loginId, input_Name, input_Age, input_Num, input_Kind, input_Gender)
                    st.success(f'{input_Name} 등록되었습니다', icon="✅")

        with tab3:
            if MemberService.loginId == '':
                st.write('로그인 먼저 하세요')
                return
            else:
                st.subheader('반려묘 정보')
                self.petsv.printCatInfo(MemberService.loginId)
                st.subheader('반려묘 정보 수정')
                input_catname = st.text_input('반려묘이름', max_chars=45,key=1)
                input_catage = st.number_input('반려묘나이', value=1, min_value=1, step=1,key=2)
                input_catkind = st.text_input('반려묘종', max_chars=20,key=3)
                input_catgender = st.text_input('반려묘성별', max_chars=5,key=4)
                editted = st.button('수정하기')
                if editted:
                    con = sqlite3.connect('mydb.db')
                    cur = con.cursor()
                    sql = 'Update Cat Set Cat_Name=?, Cat_Age=?, Cat_Kind=?,Cat_Gender=? Where User_Id=?'
                    d = (input_catname, input_catage, input_catkind, input_catgender, MemberService.loginId)
                    cur.execute(sql, d)
                    con.commit()
                    cur.close()
                    con.close()
                    return st.write('수정 완료되었습니다.')

                st.subheader('반려묘 정보 삭제')
                if st.button('삭제하기'):
                    self.petsv.delCat(MemberService.loginId)


            # if editted:
            #     if MeberService.loginId =='':
            #         st.write('로그인하고 이용하세요')
            #     else:




if __name__ == '__main__':
    m = Mypage_page()
    m.run()
