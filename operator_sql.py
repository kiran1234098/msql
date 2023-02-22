import mysql.connector

car = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

cur = car.cursor()
cur.execute("use practice")
#cur.execute("select * from practice2 where Name='sugar' and productId=1")
#for i in cur :
    #print(i)

#cur.execute("select * from practice2 where Name='sugar' or productId=1")
#for i in cur:
    #print(i)  

#cur.execute("select * from practice2 where not Name='sugar'")
#for i in cur:
    #print(i) 

#cur.execute("select * from practice2 where Name='rice' and (productId=1 or productId=2)") 
#for i in cur:
    #print(i)  

#cur.execute("select * from practice2 where Name='sugar' and not productId=1")
#for i in cur:
  #  print(i)

cur.execute("update practice2 set Name='gobhi' where productId=5 ")


