"""
    The control statements present in python are divided into:
        Conditional: if, if else, if elif(s) else
        Looping: for, while loops
        Tranfer: break, continue, pass, assert, return
"""
#if statement
if 1 == 1:
    print("We are equal")

#if-else statement
x = 0
if x > 1:
    print("I am greater than 1", x)
else:
    print("Sorry I am less than 1")

#if-elif-else
y = 2
if y == 1:
    print("I am 1")
elif y == 2:
    print("I am 2")
else:
    print("Sorry I am not 1 or 2")