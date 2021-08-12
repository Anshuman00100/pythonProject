from task import Task
from user import User
t1=Task(2,'10th Aug 2021','16th Aug 2021','python training','not completed','high',2)
u1=User(27,'Akshay','akshay@gmail.com',9865798388)


def assign_task_to_user(user,task):
    task.userid=user.userid

assign_task_to_user(u1,t1)
print(t1.userid)
print(t1.status)
print(u1.userid)
print(t1.task_description)
print(t1.start_date)
print(t1.due_date)
print(t1.task_priority)
