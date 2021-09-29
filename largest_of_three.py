# Aim:-Write a program to find largest of three numbers
a,b,c=[int(x) for x in (input("Enter any three number ").split())]
if a>b and a>c:
    print(a," is largest value")
elif b>a and b>c:
    print(b," is largest value")
else:
    print(c," is largest value")