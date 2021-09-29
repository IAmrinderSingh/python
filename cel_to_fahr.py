# Aim:-Write a python program to convert temperature to and from celsius,fahrenheit
opt = int(input(f"Enter 1 to convert temperature celsius to fahrenheit or 2 to convert temperature fahrenheit to celsius: "))
if opt==1:
    celsius = int(input("Enter tempreture in Celsius: "))
    Fahrenheit = (celsius*9/5)+(32)
    print(celsius, "degree Celsius = ", Fahrenheit, "Fahrenheit")
else:   
    Fahrenheit = int(input("Enter tempreture in Fahrenheit: "))
    celsius=(Fahrenheit-32)*5/9
    print(Fahrenheit, "degree Fahrenheit = ", celsius, "celsius")
        


