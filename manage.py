import sqlite3 as sql
import os
def viewall():
    attendance = sql.connect("attendance.db")
    atcur = attendance.cursor()
    atcur.execute("SELECT * FROM ATTENDANCE")
    attendance_table = atcur.fetchall()
    print("Attendance: ")
    print(" Name, ID, attendance ->")
    for x in attendance_table:
        print(x)
    atcur.execute("SELECT U_NAME,U_ID,CLASS,SECTION FROM STUDENTS")
    students_table = atcur.fetchall()
    print("Students: ")
    print("(Name, ID, Class, Section)")
    for x in students_table:
        print(x)
def update(id,date,action):
    attendance = sql.connect("attendance.db")
    atcur = attendance.cursor()
    atcur.execute("UPDATE ATTENDANCE SET \""+ date + "\" = "+ str(action)+ " WHERE U_ID = "+ str(id))
    print("Attendance updated")
    attendance.commit()
    trash = input("Press Enter to continue")
    os.system('cls' if os.name == 'nt' else 'clear')