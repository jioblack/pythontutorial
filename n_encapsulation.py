"""
    Encapsulation is the process of binding methods and variables together so that only those methods
    can access that data. It's about protecting an object properties/variables from other objects. 
    The encapsulation is done mostly by classes. This classes encapsulates mentods and properties/variables.
    Encapsulation involves making use of getter and setters to access and modify protected/private 
    variables in a class.
"""

class Courses:
    #Static variable
    feeling = "Happily married in a bit"

    #Parameterized Constructor
    def __init__(self, name, description, price):
        #Private variables/properties marked using double underscore (__)
        self.__name = name
        self.__description = description
        self.__price = price

    #Instance Method. Getter
    def getDescription(self):
        return self.__description

    #Instance Method. Setter
    def setDescription(self, des):
        self.__description = des

    #Instance Method. Getter
    def getName(self):
        return self.__name

    #Instance Method. Setter
    def setName(self, n):
        self.__name = n

    #Instance Method. Getter
    def getPrice(self):
        return self.__price

    #Instance Method. Setter
    def setPrice(self, pr):
        self.__price = pr

#Trying to access a private variable results in an error
myCourse = Courses("Scala","A basic introduction to programming with Scala", 20)
#print(myCourse.__name)

#Accessing private variables using getters
print(myCourse.getName())
print(myCourse.getDescription())
print(myCourse.getPrice())

#Python variables are not totally private and can be accessed using Name Mangling
#Python private variables are stored as: _ClassName__variableName
print(myCourse._Courses__name)

"""Note:
        Python variables can be made private either with single underscore(_) which is weakly private
        or double underscore(__) which is strongly private.
        Single underscored variable signals that they are private and shouldn't be used by external code.
        However it is only a convection and those not stop external code from accessing them. It however,
        prevents such variables from being imported ("from module_name import *" wont import such variables.
        Double underscored variable signals a strongly private method. This causes such variable/method to
        be mangled, which means that they can't be accessed from outside the class. In reality such variable
        can still be accessed using: _ClassName__variableName

"""