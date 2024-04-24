import sqlite3 as sql
from datetime import date
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
    cur.execute("ENTER INTO ATTENDANCE (" + str(today)+ ") VALUES (1) WHERE S_ID = \"" + user +"\"" )