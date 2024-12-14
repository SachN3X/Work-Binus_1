def Name():
    print("""
    ---------------------
    |Lucia Sachiko Toreh|
    |     Jakarta       |
    ---------------------
    """)
def Addition(Value1 = 0, Value2 = 0):
    Answer = Value1 + Value2
    return Answer
def Substraction(Value1 = 0, Value2 = 0):
    Answer = Value1 - Value2
    return Answer
def Division(Value1 = 0, Value2 = 0):
    Answer = Value1 / Value2
    return Answer
def Multiplication(Value1 = 0, Value2 = 0):
    Answer = Value1 * Value2
    return Answer
def Modulus(Value1 = 0, Value2 = 0):
    Answer = Value1 % Value2
    return Answer

while(True):
    #input float
    Operator = str(input("Enter Menu (+|-|/|*|%|stop):"))
    if (Operator == "stop"):
        print ("Program stopped. Thank you for using my program.")
        break
    Value1 = float(input("Enter Value:"))
    Value2 = float(input("Enter Value:"))
    
    if(Operator == "+"):
        Answer = Addition(Value1, Value2)
        print ("The result of substraction of",Value1, "+",Value2, "is",Answer)
    elif(Operator == "-"):
        Answer = Substraction(Value1, Value2)
        print ("The result of substraction of",Value1,"-",Value2, "is",Answer)
    elif(Operator == "/"):
        Answer = Division(Value1, Value2)
        print("The result of substraction of",Value1,"/",Value2, "is",Answer)
    elif(Operator == "*"):
       Answer=Multiplication(Value1, Value2)
       print("The result of substraction of",Value1,"*",Value2, "is",Answer)
    elif(Operator == "%"):  
        Answer= Modulus(Value1, Value2)
        print ("The result of substraction of",Value1, "%",Value2,"is",Answer)
    else:
         print ("Invalid")
         
