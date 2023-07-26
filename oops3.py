class employee:
     number_of_leaves=8
     def __init__(self, aname, asalary, arole ):
         self.name=aname
         self.salary=asalary
         self.role=arole

     def printdetails(self):
         print(f"{self.name}, {self.salary},{self.role}")

jay=employee("jay", 555, "student")
print(jay.printdetails())
