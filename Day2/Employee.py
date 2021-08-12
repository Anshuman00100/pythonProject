class Employee:
    companyname = 'Sonata Sotware ltd'
    def __init__(self, empid, name, dept):
        self.id = empid
        self.fullname  = name
        self.department = dept
        print("Super Class constructor")

    def display(self):
        print(self.id)