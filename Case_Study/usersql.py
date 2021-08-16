import mysql.connector
from case_user import user
from datetime import datetime
def connectToDB():
        mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="akpans.27", database="python")
        return mydb


def insertUser(user) :
        mydb = connectToDB()
        mycursor = mydb.cursor()
        sql = "insert into user (userid,username,role,dob,contactno,createdon,modifiedon) values(%s,%s,%s,%s,%s,%s,%s)"
        val = (user.userid,user.username,user.role,user.dob,user.contactno,user.createdon,user.modifiedon)
        #val = (100,"Anshu","Trainee",'21-22-22',999222111,'23-54-77','23-3-12')
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()


u = user(1,"Anshu","Trainee",'999222111','21-22-1998','21-22-1998','21-22-1998')
insertUser(u)