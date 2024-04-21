import sqlite3 as sql
db = sql.connect('attendance.db')
cur = db.cursor()
cur.execute("CREATE TABLE ATTENDANCE (U_NAME CHAR, U_ID INT(4) PRIMARY KEY);")
# cur.execute("INSERT INTO STUDENTS VALUES(\"Arpit\", 1234,\"Arpit123\",12,\"A\")")
db.commit()
cur.execute("SELECT * FROM ATTENDANCE")
entries = cur.fetchall()
for i in entries:
    print(i)