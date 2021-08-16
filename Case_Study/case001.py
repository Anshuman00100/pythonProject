import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "akpans.27",
    database = "testdb"
)

mycursor = mydb.cursor()

sqlformula = "INSERT INTO caseuser (userid,username,role,dob,createdon,modifiedon) VALUES (%s , %s , %s , %s ,%s , %s)"
users = [(2 , "Akshay" , "Trainee" , "21-3-98" , "21-08-21" , "23-08-21"),
         (3, "Advaith", "Trainee", "21-4-98", "21-08-21", "23-08-21"),
         (4, "Hanish", "Trainee", "21-5-98", "21-08-21", "23-08-21"),
         (5, "Swathi", "Trainee", "21-2-98", "21-08-21", "23-08-21")]

mycursor.executemany(sqlformula , users)
mydb.commit()


