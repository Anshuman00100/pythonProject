import mysql.connector
from user import User
def connectToDB():
        mydb = mysql.connector.connect(host="localhost", user="root", password="akpans.27", database="python")
        return mydb


def insertUser(user):
        mydb = connectToDB()
        mycursor = mydb.cursor()
        sql = "insert into user (username,email,phone) values(%s,%s,%s)"
        val = (user.name, user.email, user.phone)
        #val = ("Ganesh", "ganesh@sonata.com", "999999999")
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()


u = User(100,"Ganesh Babu", "ganesh@sonata.com", "999999999")
insertUser(u)