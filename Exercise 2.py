#input float
Age = int(input("Enter your age :"))
#Process
if ((Age >=0)and (Age <=1)):
    print("Baby")
elif((Age >=2)and (Age <=3)):
    print("Toddler")
elif((Age >=4)and (Age <=5)):
    print("Preschooler")
elif((Age >=6)and (Age <=12)):
    print("Child")
elif((Age >=13)and (Age <=17)):
    print("Teenager")
elif((Age >=18)and (Age <=21)):
    print("Young Adult")
elif((Age >=22)and (Age <=30)):
    print("Pre-adult ")
elif((Age >=31)and (Age <=50)):
    print("Adult")
elif((Age >=51)and (Age <=70)):
    print("Pre-elderly")
else: 
    print("Elderly") 
