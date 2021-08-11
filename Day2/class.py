class Employee:
    'Common base class for all employees'
    empCount = 0  # class variable shared by all instances

    def __init__(self, name, salary):  # constructor
        self.name = name  # instance variable unique to each instance
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


emp1 = Employee('ganesh', '5000')
emp1.displayEmployee()