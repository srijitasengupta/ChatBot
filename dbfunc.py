import mysql.connector
import random
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass",
  database="abc"
)
mycursor = mydb.cursor()
li=[]
def add_books():
	return("Enter bookname: (The format is 'Bookname is:^....^')")
def add_record(bname,aname):
	global li
	#li=[1,0]
	while(1):
		i=random.randint(0,10000)
		if i not in li:
			li.append(i)
			break
	print(li)
	sql = "INSERT INTO books (bid,book_name,author,status) VALUES (%s,%s,%s,%s)"
	val = (i, bname,aname,"Available")
	mycursor.execute(sql, val)
	mydb.commit()

def view_books():
	s="select * from books"
	mycursor.execute(s)
	result=mycursor.fetchall()
	print(result)
	st=""
	li1=[]
	li2=[]
	for i in result:
		st=""
		if i[1] not in li1:
			li1.append(i[1])
			p2=(str(i[1]))
			p='select count(*) from books where book_name="{0}"'.format(p2)
		#print(p)
			mycursor.execute(p)
			r=mycursor.fetchone()
			st+="Book name:"+str(i[1])+" by "+str(i[2])+" .No of books available = "+str(r[0])
			if int(r[0])>0:
				st+="\n You can buy the book "+i[1]+" since it is available.But hurry!\n\n"
			else:
				st+="\nBut Sorry.The book is not currently available.You may order later.Soory for the inconvenience.\n\n"
			li2.append(st)
			#print(li2)
	return "***************************\n".join(li2)
#view_books()

def buy_books(b):
		sql = "DELETE FROM books WHERE book_name = '{0}' limit 1".format(b)
		mycursor.execute(sql)
		mydb.commit()
	#print(mycursor.rowcount)
		return("You bought this book")