class User:
    "Common base class for all User"
    userCount = 0
    
    def __init__(self, name="User", score=0):
        self.name = name
        self.score = score
        User.userCount += 1
    
    def displayCount(self):
        print("Total User: %d" % User.userCount)
    
    def printUser(self):
        print("Name:", self.name, "\nScore:", self.score)
    
    # Getter Method Declaration
    def getterUser(self, parameterType):
        if parameterType == "Name":
            return self.name
        elif parameterType == "score":
            return self.score
        else:
            return "Data Not Found"
    
    # Setter Method Declaration
    def setterUser_name(self, name):
        self.name = name
    
    def setterUser_Score(self, score):
        self.score = score
    
    # Deletion Method
    def deletedUser(self):
        self.name = None
        self.score = None
        print("User Data Deleted")


# Main Code
User1 = User()

while True:
    print("""===== OOP Program =====
    1. Declare Object
    2. Display Object
    3. Change Object Value
    4. Delete Object
    5. Exit Program""")
    
    Menu = int(input("Enter Your Choice (1/2/3/4/5):"))
    
    if Menu == 1:
        Name = input("Please enter your name: ")
        Grade = int(input("Please enter your score: "))
        User1 = User(Name, Grade)  # Update User1 with new values
        User1.printUser()
    elif Menu == 2:
        User1.printUser()
        User1.displayCount()
    elif Menu == 3:
        userNew = str(input("What would you like to change (Name/Score):"))
        if userNew == "Name":
            userNew_name = str(input("Enter new Name:"))
            User1.setterUser_name(userNew_name)
            print("Name Updated Successfully.")
        elif userNew == "Score":
            userNew_score = int(input("Enter new Score:"))
            User1.setterUser_Score(userNew_score)
            print("Score Updated Successfully.")
        else:
            print("Invalid Choice.")
    elif Menu == 4:
        User1.deletedUser()
        print("Data Successfully Deleted")
    elif Menu == 5:
        print("Thank you for using my program")
        break
    else:
        print("Invalid Choice. Please Try Again.")
