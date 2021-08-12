class Task:
    """Common base class for all tasks"""
    Tcount = 0  # class variable shared by all instances

    def __init__(self,task_id, task_description, start_date, due_date, status, task_priority, userid):  # constructor
        self.task_id = task_id
        self.task_description = task_description  # instance variable unique to each instance
        self.start_date = start_date
        self.due_date = due_date
        self.status = status
        self.task_priority = task_priority
        self.userid = userid
        Task.Tcount += 1


