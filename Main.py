import Mark
import sqlite3 as sql
from datetime import date
today = date.today()
obj = sql.connect('teacher.db')
t_cur = obj.cursor()
while True:
    print("Please login....\n")
    t_user = int(input("Enter teacher id: "))
    t_pass = str(input("Enter teacher pass: "))

    t_cur.execute("SELECT * FROM TEACHER WHERE T_ID = " + str(t_user)+ " AND TPASS = \""+ t_pass + "\"")
    out = t_cur.fetchall()
    if len(out) == 0:
        print("ERROR! INVALID LOGIN")
    else:
        print("\n\n\n\n\n")
        obj.close()
        new_obj = sql.connect('attendance.db')
        newcur = new_obj.cursor()
        newcur.execute('ALTER TABLE STUDENT ADD ' + str(today) + 'INT(1);')
        new_obj.close()
        break
while True:
    print("Welocme to AMS, please select one of the following outputs: ")
    print("\nSno\t| Action\n0. \t| EXIT\n1. \t| View your attendance\n2. \t| Mark Attendance\n")
    action = int(input("\n Enter the S.no of your action: "))
    if action == 0:
        break
    elif action == 1:
        continue
    elif action == 2:
        user = Mark.validate_user()
        if user[0]:
            Mark.present(user[1])
    else:
        print("Enter valid option!!")

print("Thankyou for using!!")