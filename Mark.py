import sqlite3 as sql
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