from datetime import date
# import sqlite3 as sql
# db_att = sql.connect('attendance.db')
# cur = db_att.cursor()
today = date.today()
# cur.execute("SHOW COLUMNS FROM ATTENDANCE;")
# disc = cur.fetchall()
# print(disc)
# # Todo: fix columns method
dat = today.strftime("%d%B")
print(dat)