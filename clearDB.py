#This file deletes database
import sqlite3
import sys

conn = sqlite3.connect('myDB.db')

c = conn.cursor()

c.execute("DROP TABLE SHIPMENT")
c.execute("DROP TABLE PART")
c.execute("DROP TABLE SUPPLIER")

conn.commit()
