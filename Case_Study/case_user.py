import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "akpans.27",
    database = "testdb"
)

mycursor = mydb.cursor()

sqlformula = "INSERT INTO caseuser (userid,username,role,dob,createdon,modifiedon) VALUES (%s , %s , %s , %s ,%s , %s)"
user1 = (1 , "Anshuman" , "Trainee" , "21-2-98" , "21-08-21" , "23-08-21")

mycursor.execute(sqlformula , user1)
mydb.commit()