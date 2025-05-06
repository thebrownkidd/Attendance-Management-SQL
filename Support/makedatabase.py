import sqlite3 as sql
db = sql.connect('Databases/attendance.db')
cur = db.cursor()
# cur.execute("CREATE TABLE TEACHER (T_NAME CHAR, T_ID INT(4) PRIMARY KEY, TPASS CHAR NOT NULL)")
# cur.execute("SHOW ;")
# cur.execute("DESC TABLE TEACHER;")
# db.commit()
# cur.execute("SELECT * FROM TEACHER")
# entries = cur.fetchall()
# for i in entries:
#     print(i)
# cur.execute("SELECT * FROM STUDENTS")
# tables = cur.fetchall()
# for table in tables:
#     print(table)
cur.execute('''INSERT INTO STUDENTS VALUES ('Aditya', 1235, "Pass123", 12, 'A')''')

db.commit()
cur.execute("SELECT * FROM STUDENTS")
tables = cur.fetchall()
for table in tables:
    print(table)