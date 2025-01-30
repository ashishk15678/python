# from package.module1 import Charge
# from package.module2 import ABC
# from package import module2
# print(ABC(2)) 
# print(ABC("Name"))
# print(module2.ABC(2))
# print("Ashish kumar",sep="|",end=" ")
# for i in "Ashish Kumar":
#     print(i,end=" ")
# print("\n")

class Student:
    name:str
    Class:int

    def __init__(self, name, Class):
        self.name = name
        self.Class = Class

    def lowerClass(self):
        self.Class = self.Class - 1

class newStudent:
    name:str
    erp:str

    def __init__(self,name,erp):
        self.name = name
        self.erp = erp
    
    def ChangeErp(self,newErp):
        self.erp = newErp
        

student1 = Student("John Doe", 10)
student1.lowerClass()
print(student1.Class)
thisTuple = (1,2,3)
print(thisTuple)