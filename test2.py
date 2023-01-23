import mysql.connector

car = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

cur = car.cursor()
cur.execute("select * from fsds_db.fsds1")

for i in cur:
    print(i)

cur.execute("UPDATE fsds_db.fsds1 SET mail_id ='kiran@gmail.com' ")   
cur.execute("select * from fsds_db.fsds1")

for i in cur:
    print(i)