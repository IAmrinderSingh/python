height, base, hypotenuse = [int(x) for x in input(
    "Enter height,base and hypotenuse respectively: ").split()]
if(height**2+base**2 == hypotenuse**2):
    print("It is right triangle")
else:
    print("It is not a right triangle")
    
