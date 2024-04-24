import Mark
import sqlite3 as sql
from datetime import date
import os
import manage
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
os.system('cls' if os.name == 'nt' else 'clear')
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
        today = today.strftime("%d%B")
        command = "ALTER TABLE ATTENDANCE ADD \"" + str(today) + "\" INT(1) DEFAULT 0;"
        newcur.execute(command)
        new_obj.close()
        os.system('cls' if os.name == 'nt' else 'clear')
        break
while True:
    print("Welocme to AMS, please select one of the following outputs: ")
    print("\nSno\t| Action\n0. \t| EXIT\n1. \t| View your attendance\n2. \t| Mark Attendance\n3. \t| Admin Menu")
    action = int(input("\n Enter the S.no of your action: "))
    if action == 0:
        break
    elif action == 1:
        user= Mark.validate_user()
        if user[0]:
            a = Mark.view_attendance(user[1])
            print(a)
            trash = input("Press enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Invalid Login!!")
    elif action == 2:
        user = Mark.validate_user()
        if user[0]:
            Mark.present(user[1])
        else:
            print("Invalid Login!!\n")
    elif action == 3:
        admin = True
        while admin:
            print("Plese Valudate yourself")
            t_user = int(input("Enter your admin id: "))
            t_pass = str(input("Enter your password: "))
            obj = sql.connect('teacher.db')
            t_cur = obj.cursor()
            t_cur.execute("SELECT * FROM TEACHER WHERE T_ID = " + str(t_user)+ " AND TPASS = \""+ t_pass + "\"")
            out = t_cur.fetchall()
            if len(out) == 0:
                print("\n\nERROR! INVALID LOGIN")
                print("Redirecting to general menu.....\n\n")
            else:
                while admin:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Welcome to admin menu.... ")
                    print("\n1.\t| Exit to Genetal menu\n2.\t| View attendance record\n3.\t| Update attendance\n4.\t| Remove student\n5.\t| Full access mode\n\n")
                    opt = int(input("Select an option: "))
                    if opt == 1:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        admin = False
                        break
                    elif opt == 2:
                        manage.viewall()
                    elif opt == 3:
                        upd_id = int(input("Enter the id of student you wanna mark: "))
                        upd_month= monthbynumber[int(input("Enter the month: "))]
                        upd_day = int(input("Enter the day of the month: "))
                        upd_date = str(upd_day) + upd_month 
                        action = int(input("Enter the amount of attendance this day holds: "))
                        manage.update(upd_id,upd_date,action)
                    elif opt == 4:
                        user = int(input("Enter id of student you want to remove: "))
                        manage.remove(user)
                    elif opt == 5:
                        manage.fullaccess()
                    else:
                        print("Invalid input")
    else:
        print("Enter valid option!!")

print("Thankyou for using!!")