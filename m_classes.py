"""
Object Oriented Programming (OOP) is a programming paradigm based on the concept of "objects"
which can contain data in the form of fileds/variables, and code in the form of procedures/methods/functions.
OOP contain four basic concept:
    1. Encapsulation
    2. Polymorphism
    3. Abstraction
    4. Inheritance
and makes use of Classes as blueprint on which objects are built
"""
"""
Classes allow for the creation of user defined data types. They act as a blue print for our objects.
Classes contain: variable aka instance variable
                 methods aka instance method
                 static variables: variables that be accessed using the Class name directly 
"""


class Course:
    #Constructor
    def __init__(self):
        self.name = "Python"
        self.description = "An Introduction to Python"
        self.price = 20


p1 = Course()
print(p1.name)
print(p1.description)
print(p1.price)


class Courses:

    #Static variable. This variables can be from an Instance of the class
    feeling = "Happily married in a bit"

    #Parameterized Constructor
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    #Instance Method.
    def halfPrice(self):
        return self.price / 2

    #Instance Method. Getter
    def getDescription(self):
        return self.description

    #Instance Method. Setter
    def setDescription(self, des):
        self.description = des

    #Inner Class
    class Author:
        def __init__(self,name,age):
            self.name=name
            self.age=age


#Creating Objects from Courses class
p2 = Courses("Java", "The basics of Java", 10)
p3 = Courses("JavaScript", "Basic JavaScript Concept", 15)
print(p2.name)
print(p2.description)
print(p3.price)

#Calling static variable
print(Courses.feeling)

#Accessing Inner classes
p2Author=p2.Author("Enobong",27)
p3Author=p3.Author("Ifere",31)

"""
Advanced Topics: class and static methods. 
Class methods are called by a class which is passed to the cls parameter of the method and not by an
instance of a class which is then passed to the self parameter of the method as earlier methods we have
seen do. Class methods are marked with a @classmethod decorator.
Static methods are similar to class methods except they don't receive any additional arguments, they are
identical to normal functions that belong to a class. Static method are marked with the @staticmethod
decorator
"""

class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def calc_area(self):
        return self.width*self.height

    #Declaring a class method: The method is called on the class instead of an instance of the class
    #and it return a new object of the class cls
    @classmethod
    def square(cls,length):
        return cls(length,length)

    #Declaring a static method call.
    @staticmethod
    def display():
        print("The is a Static method call")

square1 = Rectangle.square(10)
print(square1.calc_area())
Rectangle.display()