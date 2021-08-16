
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="akpans.27",
    database="python"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customer (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
val = ("Ganesh", "Banglore")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM customer")
myresult = mycursor.fetchall()
print(myresult)
print("Name |  Address")
for x in myresult:
    print(x[0] + " | " + x[1])
    print(type(x))
mydb.close()
