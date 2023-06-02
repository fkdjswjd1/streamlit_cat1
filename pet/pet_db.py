import streamlit as st
import sqlite3
from pet.cat import Pet

class PetDao:
    # Cat 테이블 생성 : 한번만 실행
    con=sqlite3.connect('mydb.db')
    cur=con.execute("""
    create table Cat(
    User_Id char(15),
    Cat_Name char(45),
    Cat_Age int,
    Cat_Num char(20) primary key,
    Cat_Kind char(20),
    Cat_Gender char(5),
    FOREIGN KEY('User_Id') REFERENCES 'User'('User_Id') ON DELETE CASCADE)
    """)
    cur.close()
    con.close()
    def insert(self, a:Pet): # 추가 메서드
        con=sqlite3.connect('mydb.db')
        cur=con.cursor()
        cur.execute(f'INSERT INTO Cat (User_Id,Cat_Name,Cat_Age,Cat_Num,Cat_Kind,Cat_Gender) VALUES("{a.User_Id}","{a.Cat_Name}","{a.Cat_Age}","{a.Cat_Num}","{a.Cat_Kind}","{a.Cat_Gender}")')
        con.commit()
        cur.close()
        con.close()

    def select(self,User_Id):# User_Id기준으로 검색메서드
        con = sqlite3.connect('mydb.db')
        cur = con.cursor()
        try:
            cur.execute(f'select * from Cat where User_Id="{User_Id}"')
            cat_info=cur.fetchone()
            if cat_info:
                return Pet(cat_info[0],cat_info[1],cat_info[2],cat_info[3],cat_info[4])
        except Exception as e:
            st.write(e)
        finally:
            cur.close()
            con.close()


    def delete(self, User_Id:str): #User_Id기준으로 삭제메서드
        con = sqlite3.connect('mydb.db')
        cur = con.cursor()
        try:
            cur.execute(f'delete from Cat where User_Id="{User_Id}"')
            con.commit()
            return st.write('삭제가 완료되었습니다.')
        except Exception as e:
            st.write(e)
        finally:
            cur.close()
            con.close()
