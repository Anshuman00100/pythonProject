class User:
    """Common base class for all Users"""
    Ucount = 0  # class variable shared by all instances

    def __init__(self, userid, user_name, email, phone_number):  # constructor
        self.userid = userid
        self.name = user_name
        self.email = email
        self.ph_no = phone_number

        User.Ucount += 1
