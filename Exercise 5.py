import math
#input the value
a = float(input("Masukan Nilai A: "))
b = float(input("Masukan Nilai B: "))
c = float(input("Masukan Nilai C: "))
if a == 0:
    if a == 0:
     print("Bukan persamaan kuadrat.")
else:
    print(f"Persamaan kuadrat:"+ str(a) + "x² + " + str(b) + "x + " + str(c) + " = 0")
    D = b**2 - 4*a*c
    print("Determinannya:"+ str(D))
    if D > 0:
        x1 = (-b + D**0.5) / (2 * a)
        x2 = (-b - D**0.5) / (2 * a)
        print("Merupakan Akar Berbeda:")
        print("Akar x1 =" + str(x1))
        print("Akar x2 ="+ str(x2))
    elif D == 0:
        x = -b / (2 * a)
        print("Determinannya =" +str(D))
        print("Merupakan Akar Kembar:")
        print("Akar =" + str(x2))
    elif (D < 0):
        print("Merupakan Akar Imajiner:")
        x1 = "(-" + str(b) + " + √(" + str(D) + ")) / (2*" + str(a) + ")"
        x2 = "(-" + str(b) + " - √(" + str(D) + ")) / (2*" + str(a) + ")"
        print("Akar x1 =" + str(x1))
        print("Akar x2 =" + str(x2))
    else:
        print ("It is not a quadratic equation")
