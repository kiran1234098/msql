import mysql.connector

car = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

cur = car.cursor()
cur.execute("create database practice")

cur.execute("use practice")
cur.execute("create table practice1 (Firstname varchar(50),SecondName varchar(50),email varchar(70),password int)")
cur.execute("insert into practice1 values('kiran','zapate','kjcomprac@gmail.com',123)")

car.commit()
cur.execute("select * from practice1")

for i in cur:
    print(i)

#cur.execute("select Firstname from practice1")
#for i in cur:
   # print(i)

cur.execute("insert into practice1 values('priyanka','zapate','kiran2@gmail.com',678)")  
car.commit()  
#cur.execute("select distinct Firstname from practice1")
#for i in cur:
    #print(i)

#cur.execute("select count(distinct Firstname) from practice1")  
#for i in cur:
    #print(i) 

#cur.execute("select * from practice1 where email='kiran@gmail.com'")
#for i in cur:
    #print(i)
#cur.execute("select * from practice1 where password=123")  
#for i in cur:
    #print(i)  
cur.execute("create table practice2 (productId int,Name varchar(50),price int,country varchar(50))")
cur.execute("insert into practice2 values(3,'poteto',100,'india')")

car.commit()

#cur.execute("select * from practice2")
#for i in cur:
    #print(i)

#cur.execute("select * from practice2 where price between 70 and 100")
#for i in cur:
    #print(i)   
#cur.execute("select * from practice2 where Name like 's%'")
#for i in cur:
    #print(i) 

cur.execute("select * from practice2 where Name in ('sugar','rice')")
for i in cur:
    print(i)    
