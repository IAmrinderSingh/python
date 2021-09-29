# write a python program to construct the following pattern using nested for loop
# *
# *
# **
# ***
# ****
# ***
# **
# *
# *
for i in range(5):
    for j in range(i):
        print("*",end='')
    print('\n')
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end='')
    print('\n')
