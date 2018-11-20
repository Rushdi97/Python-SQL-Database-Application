#This file creates a Database and inserts neccesary info
import sqlite3
import sys

conn = sqlite3.connect('myDB.db')

c = conn.cursor()

c.execute("CREATE TABLE SUPPLIER(Sno VARCHAR(4) PRIMARY KEY,Sname VARCHAR(6) NOT NULL,Stat INT CHECK (Stat >= 0),City VARCHAR(6));")
c.execute("CREATE TABLE PART(Pno VARCHAR(4) NOT NULL,Pname VARCHAR(255) NOT NULL,Color VARCHAR(255),Wght INT CHECK (Wght >= 1 AND Wght <= 100),City VARCHAR(255),PRIMARY KEY(Pno));")
c.execute("CREATE TABLE SHIPMENT(Sno VARCHAR(4),Pno VARCHAR(4),Qty  INT check (Qty >= 0) DEFAULT 100,Price DECIMAL(10,3),PRIMARY KEY(Sno,Pno));")

#c.execute("ALTER TABLE PART ADD CONSTRAINT myConstraint UNIQUE(Pname,Color)")

#load
c.execute("INSERT INTO SUPPLIER (Sno, Sname, Stat, City) VALUES('s1','Smith',20,'London')")
c.execute("INSERT INTO SUPPLIER (Sno, Sname, Stat, City) VALUES('s2','Jones',10,'Paris')")
c.execute("INSERT INTO SUPPLIER (Sno, Sname, Stat, City) VALUES('s3','Blake',30,'Paris')")
c.execute("INSERT INTO SUPPLIER (Sno, Sname, Stat, City) VALUES('s4','Clark',20,'London')")
c.execute("INSERT INTO SUPPLIER (Sno, Sname, Stat, City) VALUES('s5','Adams',30,NULL)")
c.execute("INSERT INTO PART(Pno,Pname,Color,Wght,City) VALUES('p1','Nut','Red', 12 , ' London')")
c.execute("INSERT INTO PART(Pno,Pname,Color,Wght,City) VALUES('p2','Bolt','Green', 17 , ' Paris')")
c.execute("INSERT INTO PART(Pno,Pname,Color,Wght,City) VALUES('p3','Screw',NULL, 17 , ' Rome')")
c.execute("INSERT INTO PART(Pno,Pname,Color,Wght,City) VALUES('p4','Screw','Red', 14 , ' London')")
c.execute("INSERT INTO PART(Pno,Pname,Color,Wght,City) VALUES('p5','Cam','Blue', 12 , ' Paris')")
c.execute("INSERT INTO PART(Pno,Pname,Color,Wght,City) VALUES('p6','Cog','Red', 17 , ' London')")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s1', 'p1', 300, .005)")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s1', 'p2', 200, .009)")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s1', 'p3', 400, .004)")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s1', 'p4', 200, .009)")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s1', 'p5', 100, .01)")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s1', 'p6', 100, .01)")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s2', 'p1', 300, .006)")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s2', 'p2', 400, .004)")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s3', 'p2', 200, .009)")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s3', 'p3', 200, NULL)")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s4', 'p2', 200, .008)")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s4', 'p3', NULL, NULL)")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s4', 'p4', 300, .006)")
c.execute("INSERT INTO SHIPMENT(Sno, Pno,Qty,Price) Values('s4', 'p5', 400, .003)")

conn.commit()
