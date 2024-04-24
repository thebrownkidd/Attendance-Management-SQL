import sqlite3 as sql
db = sql.connect('attendance.db')
cur = db.cursor()
# cur.execute("CREATE TABLE TEACHER (T_NAME CHAR, T_ID INT(4) PRIMARY KEY, TPASS CHAR NOT NULL)")
cur.execute("INSERT INTO ATTENDANCE VALUES(\"ARPIT\", 1234)")
db.commit()
cur.execute("SELECT * FROM ATTENDANCE")
entries = cur.fetchall()
for i in entries:
    print(i)