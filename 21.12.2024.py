class Student:
    "Common base class for all student"
    rollNum = 0
    
    def __init__(self, name="Student",age=0,nik=0):
        self.name = name
        self.age = age
        self.nik = NIK
        Student.rollNum += 1
        
    def displayCount(self):
        print("Total Student: %d" % Student.rollNum)
    
    def printStudent(self):
        print("Name:", self.name, "\nage:", self.age, "\nnik",self.nik)
        
Name = str(input("Enter your Name:"))
Age = str(input("Enter your Age:"))
nik = str(input("Enter your NIK:"))

Student = Student(Name, Age, nik)
Student.displayCount()
Student.printStudent()
