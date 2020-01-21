#Defining a function
def sqx(x):
    #Return the square of x
    return x**2


def multiargs():
    a = 2
    b = 5
    c = 8
    #Return multiple arguments
    return a * b, a * c, b * c


f = multiargs()
print(f[0])
print(f[1])
print(f[2])
print(f)

#Local and Global variable: The locals() and globals()
# functions contains all local and global variables respectively

x = 10  #Global variable


def abc():
    y = 7  #Local variable
    print(x, y)
    print(
        globals()['x']
    )  #Access the global variable 'x' using globals(variablename) function


abc()


#Function with keyword arguments
def times2(x):
    return x * 2


print(times2(x=5))  #Keyword arguments


#Default keyword arguments
def times3(a=1):
    return a * 3


print(times3())
print(times3(5))


def axb(a, b):
    return a * b


print(axb(b=15, a=10))
#
#
"""
    Assigning functions to variables, function inside function
    & returning function
"""
#Assigning functions to a variable
# We would assign axb function to a variable 'z'

z = axb

#Use the function
print(z(2, 20))


#Function inside a function
def myFunc(name):
    def insideMyFunc():
        return "Hello "

    return insideMyFunc() + name


print(myFunc("James"))


#Returning a function
def outsideFunc():
    def insideFunc(n):
        return "Hello " + n

    return insideFunc


print(outsideFunc()("Ink"))