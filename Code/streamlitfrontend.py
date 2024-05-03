import Mark
import sqlite3 as sql
from datetime import date
import os
import manage
import streamlit as st
monthbynumber = {
    1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5: 'May',
    6 : 'June',
    7 : 'July',
    8 : 'August',
    9: 'September',
    10 : 'October',
    11 : 'November',
    12 : 'December'
}
today = date.today()
obj = sql.connect('Databases/teacher.db')
t_cur = obj.cursor()
# while True:
st.text("Please login....\n")
t_user = st.number_input("Enter teacher id: ")
t_pass = st.text_input("Enter teacher pass: ")

t_cur.execute("SELECT * FROM TEACHER WHERE T_ID = " + str(t_user)+ " AND TPASS = \""+ t_pass + "\"")
out = t_cur.fetchall()
while st.button("Login"):
    if len(out) == 0:
        st.error("ERROR! INVALID LOGIN")
    else:
        # print("\n\n\n\n\n")
        obj.close()
        new_obj = sql.connect('Databases/attendance.db')
        newcur = new_obj.cursor()
        today = today.strftime("%d%B")
        command = "ALTER TABLE ATTENDANCE ADD \"" + str(today) + "\" INT(1) DEFAULT 0;"
        newcur.execute(command)
        new_obj.close()
        os.system('cls' if os.name == 'nt' else 'clear')
        st.title("Welcome to Attendance managemtn")
        
        break
