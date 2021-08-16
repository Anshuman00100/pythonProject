class user:
    """Common base class for all Users"""
    Ucount = 0  # class variable shared by all instances

    def __init__(self,userid,username,role,dob,createdon,modifiedon):  # constructor
        self.userid = userid
        self.username = username
        self.role = role
        self.dob=dob
        self.createdon = createdon
        self.modifiedon=modifiedon


        user.Ucount += 1

class Task:
    """Common base class for all tasks"""
    Tcount = 0  # class variable shared by all instances

    def __init__(self,task_id, name, description,
                    status, priority, notes,
                    bookmark, owner_id, creator_id,created_on,
                    modified_on):  # constructor
        self.task_id = task_id
        self.name = name  # instance variable unique to each instance
        self.description = description
        self.status = status
        self.priority = priority
        self.notes = notes
        self.bookmark = bookmark
        self.owner_id = owner_id
        self.creator_id = creator_id
        self.created_on = created_on
        self.modified_on = modified_on
        Task.Tcount += 1