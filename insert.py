#inserts more stuff into database
import sqlite3
import sys

conn = sqlite3.connect('myDB.db')

c = conn.cursor()

c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s2', 'p3', 200, 0.006)")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s4', 'p2', 100, 0.005)")

conn.commit()
