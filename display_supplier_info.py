#THIS FILE DISPLAYS ALL THE INFORMATION FOR THE SUPPLIER TABLE
import sqlite3
import sys

conn = sqlite3.connect('myDB.db')

c = conn.cursor()

c.execute("SELECT * FROM SUPPLIER")
res = c.fetchall()
for r in res:
    print(r)
