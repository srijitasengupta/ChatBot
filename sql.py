import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass",database="abc"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE abc")
mycursor.execute("CREATE TABLE books (bid varchar(255) primary key,book_name VARCHAR(255), author VARCHAR(255),status varchar(255))")
