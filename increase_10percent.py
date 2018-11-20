# THIS FILE UPDATES SUPPLIERS STATUS BY 10%
import sqlite3
import sys

conn = sqlite3.connect('myDB.db')

c = conn.cursor()

c.execute("UPDATE SUPPLIER SET STAT = STAT * 1.10")

conn.commit()