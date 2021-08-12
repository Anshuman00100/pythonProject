

import Day2.Employee


class Tech(Day2.Employee):
    def __int__(self , id , name , dept , skill):
        super().__init__(id, name, dept)
        self.skill = skill
        print("Sub class constructor")


t = Tech(100, "Ganesh", "Trng", "Pthon")
print(t.id)
