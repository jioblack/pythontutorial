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

    #Static variable
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