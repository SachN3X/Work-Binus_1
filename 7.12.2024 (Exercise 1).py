while(True):
#input float
    Number = float(input("Input any Number :"))
    if (Number % 2 == 0):
        print("Even")
    else:
        print("Odd")
    repeat = input("Do you want to repeat? (answer using Y/N) =")
    if (repeat == "N"):
        print ("Program Stops")
        print ("Thank you for using my program ^^")
        break
