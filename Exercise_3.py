print("1. Celsius to Fahrenheit")
print("2. Celsius to Kevin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")
Temperature = float(input("Enter Temperature:"))
Menu = int(input("Enter menu option (just enter the number):"))
if (Menu == 1):
    Fahrenheit = (9/5*Temperature)+32
    print (Fahrenheit,"°F")
elif (Menu == 2):
    Kelvin = Temperature+32
    print (Kelvin,"K")
elif (Menu == 3):
    Celcius = Temperature+273
    print (Celcius,"°C")
elif (Menu == 4):
    Kelvin = 5/9*(Temperature - 32) + 273.15
    print (Kelvin,"K")
elif (Menu == 5):
    Celcius = Temperature-273.15
    print (Celcius,"°C")
elif(Menu == 6):
    Fahrenheit = (Temperature-273.15)*9/5+32
    print (Fahrenheit,"°F") 
    
