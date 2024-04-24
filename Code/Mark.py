import sqlite3 as sql
from datetime import date
import os
def validate_user():
    user = int(input("Enter your roll no: "))
    pas = str(input("Enter the login code: "))
    db_att = sql.connect('attendance.db')
    cursor = db_att.cursor()
    command = "SELECT * FROM STUDENTS WHERE U_ID = " + str(user) + " AND PASS = \"" + pas + "\";"
    # print(command)
    cursor.execute(command)
    val = cursor.fetchall()
    if len(val) == 0:
        return [False,user]
    else:
        return [True,user]
def present(user):
    db_att = sql.connect('attendance.db')
    cur = db_att.cursor()
    today = date.today()
    # cur.execute('DESCRIBE TABLE ATTENDANCE;')
    # disc = cur.fetchall()
    # att = []
    # for x in disc:
    #     att.append(x[0])
    today = today.strftime("%d%B")
    # cur.execute("SELECT * FROM ATTENDANCE WHERE U_ID = "+ str(user))
    # data = cur.fetchall()
    # for x in data:
    #     print("Entry: ")
    #     print(x)
    cur.execute("UPDATE ATTENDANCE SET \"" + str(today)+ "\" = 1 WHERE U_ID = " + str(user))
    db_att.commit()
    print("Marked present for this user")
    Trash = input("press enter to continue")
    os.system('cls' if os.name == 'nt' else 'clear')
def view_attendance(user):
    db_att = sql.connect('attendance.db')
    cur = db_att.cursor()
    cur.execute("SELECT * FROM ATTENDANCE WHERE U_ID = "+str(user))
    ret = cur.fetchall()
    return ret