"""
Decorators are used to add/modify an existing object. They take in functions
and return functions

Format is:
        def myDecorFuncName(fun)
"""


#Decorator that doubles the result of a function.
def decorFunc(func):
    def internal():
        result = func()
        return result * 2

    return internal


#Let define a function that would use the decorator function
def decorMe():
    return 7


#Use the decorator function to decorate the decoreMe function.
d = decorFunc(decorMe)
print(d())
"""
    Using @Decorator 
    Apply the decorFunc function using @decorFunc
"""
@decorFunc
def decorMeAgain():
    return 8


print(decorMeAgain())
"""
    Decorating a String
    This example shows how to pass an argument to a decorator functions
"""


def decorString(func):
    def internal(n):
        return func(n) + " how are you?"

    return internal


@decorString
def deccorMyString(n):
    return 'Hello ' + n


print(deccorMyString("John"))