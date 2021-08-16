import mysql.connector

def connectToDB():
        mydb = mysql.connector.connect(host="localhost", user="root", password="akpans.27", database="python")
        return mydb

