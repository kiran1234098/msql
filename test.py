import mysql.connector

car = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(car.is_connected())
cur = car.cursor()
a=cur.execute("show Databases")
for i in cur:
    print(i)