import sqlite3 as sql
db = sql.connect('Databases/attendance.db')
cur = db.cursor()
# cur.execute("CREATE TABLE TEACHER (T_NAME CHAR, T_ID INT(4) PRIMARY KEY, TPASS CHAR NOT NULL)")
cur.execute("ALTER TABLE ATTENDANCE DROP COLUMN \"24April\"")
db.commit()
cur.execute("SELECT * FROM ATTENDANCE")
entries = cur.fetchall()
for i in entries:
    print(i)