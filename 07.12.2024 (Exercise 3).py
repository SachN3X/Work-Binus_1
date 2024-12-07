tampungInput = 0;
tampungNilai = 0;

while(True):
    Inputan = (input("Enter Grade(Press Enter to Stop):"))
    if (Inputan == ""):
        hasil = tampungNilai/tampungInput
        print(hasil)
        break
        if hasil >= 4.00:
            grade = "A"
        elif hasil >= 3.75:
            grade = "A-"
        elif hasil >= 3.50:
            grade = "B+"
        elif hasil >= 3.00:
            grade = "B"
        elif hasil >= 2.75:
            grade = "B-"
        elif hasil >= 2.50:
            grade = "C+"
        elif hasil >= 2.00:
            grade = "C"
        elif hasil >= 1.75:
            grade = "C-"
        elif hasil >= 1.50:
            grade = "D"
        else:
            grade = "E"
        print ("The Average Grade is:",(hasil),"With a designation:",(grade))

    else:
        if (Inputan == "A"):
            tampungNilai = tampungNilai + 4.00
            tampungInput += 1
        elif (Inputan == "A-"):
            tampungNilai = tampungNilai + 3.75
            tampungInput += 1
        elif (Inputan == "B+"):
            tampungNilai = tampungNilai + 3.50
            tampungInput += 1
        elif (Inputan == "B"):
            tampungNilai = tampungNilai + 3.00
            tampungInput += 1
        elif (Inputan == "B-"):
            tampungNilai = tampungNilai + 2.75
            tampungInput += 1
        elif (Inputan == "C+"):
            tampungNilai = tampungNilai + 2.50
            tampungInput += 1
        elif (Inputan == "C"):
            tampungNilai = tampungNilai + 2.00
            tampungInput += 1
        elif (Inputan == "C-"):
            tampungNilai = tampungNilai + 1.75
            tampungInput += 1
        elif (Inputan == "D"):
            tampungNilai = tampungNilai + 1.50
            tampungInput += 1
        else:
            print ("invalid")
    
