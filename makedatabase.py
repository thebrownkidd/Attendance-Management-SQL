import sqlite3 as sql
db = sql.connect('teacher.db')
cur = db.cursor()
cur.execute("CREATE TABLE TEACHER (T_NAME CHAR, T_ID INT(4) PRIMARY KEY, TPASS CHAR NOT NULL)")
cur.execute("INSERT INTO TEACHER VALUES(\"SOMETEACHER\", 1234,\"Pass123\")")
db.commit()
cur.execute("SELECT * FROM TEACHER")
entries = cur.fetchall()
for i in entries:
    print(i)