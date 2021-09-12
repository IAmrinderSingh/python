# Aim:-Write a program to perform different Arithmetic Operations on numbers in python
num1,num2=[int(x) for x in input("Enter any two numbers: ").split()]
add=num1+num2
diff=num1-num2
mul=num1*num2
div=num1/num2
expo=num1**num2
floor_div=num1//num2
modulus=num1%num2
print("Addition of ",num1," and ",num2," is ",add)
print("Diffrence of ",num1," and ",num2," is ",diff)
print("Product of ", num1, " and ", num2, " is ", mul)
print("Division of ", num1, " and ", num2, " is ", div)
print("exponent of ", num1, " and ", num2, " is ", expo)
print("floor Division of ", num1, " and ", num2, " is ", floor_div)
print("Modulus of ", num1, " and ", num2, " is ", modulus)
