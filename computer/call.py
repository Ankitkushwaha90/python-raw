import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="", passwd="", database="ankit")
mycursor = mydb.cursor()

mycursor.execute("select * from students")

result = mycursor.fetchone()
for i in mycursor:
	print(i)