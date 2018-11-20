#This file asks for user input and returns suppliers info that ship corressponding part number
import sqlite3
import sys

conn = sqlite3.connect('myDB.db')

c = conn.cursor()

Pnum = input("Please enter in Part number: ")

if Pnum == "p1":
    c.execute("SELECT * FROM SUPPLIER WHERE SNO IN (SELECT Sno FROM SHIPMENT WHERE Pno = 'p1')")
elif Pnum == "p2":
    c.execute("SELECT * FROM SUPPLIER WHERE SNO IN (SELECT Sno FROM SHIPMENT WHERE Pno = 'p2')")
elif Pnum == "p3":
    c.execute("SELECT * FROM SUPPLIER WHERE SNO IN (SELECT Sno FROM SHIPMENT WHERE Pno = 'p3')")
elif Pnum == "p4":
    c.execute("SELECT * FROM SUPPLIER WHERE SNO IN (SELECT Sno FROM SHIPMENT WHERE Pno = 'p4')")
elif Pnum == "p5":
    c.execute("SELECT * FROM SUPPLIER WHERE SNO IN (SELECT Sno FROM SHIPMENT WHERE Pno = 'p5')")
elif Pnum == "p6":
    c.execute("SELECT * FROM SUPPLIER WHERE SNO IN (SELECT Sno FROM SHIPMENT WHERE Pno = 'p6')")


res = c.fetchall()
for r in res:
    print(r)
