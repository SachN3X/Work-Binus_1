while(True):
#input float
    side_A = int(input("Side A (heigt/adj):"))
    side_B = int(input("Side B (hyp):"))
    side_C = int(input("Side C(base):"))
    if (side_A == side_B == side_C):
        print ("Equilateral")
    elif side_A == side_B or side_A == side_C or side_C == side_B :
        print ("Isosceles")
    elif side_A+side_B<=side_C or side_A+side_C<=side_B or side_B+ side_C<=side_A :
        print ("Not a Triangle")
    elif side_A**2 == side_B**2 + side_C**2 or side_B**2 == side_A**2 + side_C**2 or side_C**2 == side_A**2 + side_B**2 :
        print ("Right-Angled")
    else:
        print("Scalene")
    repeat = input("Do you want to repeat? (answer using Y/N) =")
    if (repeat == "N"):
        print ("Program Stops")
        print ("Thank you for using my program ^^")
        break
