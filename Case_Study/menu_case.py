import mysql.connector
from Case_Study.user import user , Task

func = input(""" Choose one:
          i.  Create User
          ii. Update User
          iii.Create Task
          iv. Update Task
        """)


def ConnectToDB():
    db = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='akpans.27',
        database='case'
    )
    return db


def i(): # create user
    mydb = ConnectToDB()
    mycursor = mydb.cursor()
    mycursor.execute(
        "CREATE TABLE user (userid INT, user_name VARCHAR(20), role VARCHAR(20), dob VARCHAR(20), created_on  VARCHAR(20),modified_on VARCHAR(20))")
    mydb.commit()
    return mycursor


def ii(user_task_classes):  # updating user
    mydb = ConnectToDB()
    mycursor = mydb.cursor()
    sql = "INSERT INTO user (userid, user_name, role, dob, created_on, modified_on) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (user_task_classes.userid, user_task_classes.username, user_task_classes.role, user_task_classes.dob,
           user_task_classes.created_on, user_task_classes.modified_on)
    mycursor.execute(sql, val)
    mydb.commit()


def iii():   # creating task
    mydb = ConnectToDB()
    mycursor = mydb.cursor()
    mycursor.execute(
        'CREATE TABLE task (task_id INT, name VARCHAR(20), description VARCHAR(255), status VARCHAR(20), priority INT, '
        'notes VARCHAR(255), bookmark VARCHAR(20), owner_id INT, creator_id INT, created_on VARCHAR(20), '
        'modified_on VARCHAR(20))')
    mydb.commit()
    return mycursor


def iv(user_task_classes):  # update task
    mydb = ConnectToDB()
    mycursor = mydb.cursor()
    sql = "INSERT INTO task (task_id, name, description, status, priority, notes, bookmark, owner_id, creator_id, " \
          "created_on, modified_on) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (user_task_classes.task_id, user_task_classes.name, user_task_classes.description, user_task_classes.status,
           user_task_classes.priority, user_task_classes.notes, user_task_classes.bookmark, user_task_classes.owner_id,
           user_task_classes.creator_id, user_task_classes.created_on, user_task_classes.modified_on)
    mycursor.execute(sql, val)
    mydb.commit()


"""
if func in locals():
    todo = locals()[func]
    todo()"""

if func == 'i':
    i()
elif func == 'ii':
    userid = int(input('Enter the userid: '))
    username = input('Enter the username: ')
    role = input('Enter the role: ')
    dob = input('Enter the dob: ')
    created_on = input('Enter created_on: ')
    modified_on = input('Enter modified_on ')
    user1 = user(userid, username, role, dob,
                    created_on, modified_on)
    ii(user1)
elif func == 'iii':
    iii()
else:
    task_id = int(input('Enter the task_id: '))
    name = input('Enter the name: ')
    description = input('Enter the description: ')
    status = input('Enter the status: ')
    priority = int(input('Enter the priority of the task: '))
    notes = input('Enter the notes: ')
    bookmark = input('Is it bookmarked? : ')
    owner_id = int(input('Enter the owner_id: '))
    creator_id = int(input('Enter the creator_id: '))
    created_on = input('Enter created_on: ')
    modified_on = input('Enter modified_on: ')
    task1 = Task(task_id, name, description,
                    status, priority, notes,
                    bookmark, owner_id, creator_id,created_on,
                    modified_on)
    iv(task1)

