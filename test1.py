import mysql.connector

car = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

cur = car.cursor()
cur.execute("create database fsds_db")
cur.execute("use fsds_db")
cur.execute("create table fsds1(name varchar(40),roll_no int,mail_id varchar(40))")
cur.execute("insert into fsds1 values('kiran',70,'kiran')")
car.commit()
cur.execute("select * from fsds1")