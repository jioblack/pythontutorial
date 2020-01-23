"""Abstraction: It involves selecting data from a larger pool to show only the relevant details 
                to the object. Abstraction can be implemented using abstract classes and interfaces 
                in most programming languages. 
                In python, an abstract class is a class that contain at least one method decorated with 
                @abstractmethod decorator. An interface is a class with all its method decorated with 
                @abstractmethod decorator.
                To define an abstract class, we inherit the "ABC" class and decorate our methods with the 
                "abstractmethod" decorator from the "abc" module
                Abstract class can be implemented by first inheriting the class and then implementing all
                the abstract methods in the class.
"""

from abc import ABC, abstractmethod
#Declaring an Abstract Interface
class Course:
    def __init__(self,name,lecturer):
        self.name=name
        self.lecturer=lecturer
    
    @abstractmethod
    def time(self):
        pass

    @abstractmethod
    def venue(self):
        pass

#Inheriting an abstract interface and implementing its abstract methods
class ELE712(Course):
    
    def time(self):
        print("This course holds on Monday, Wednesday and Fridays by 12am")

    def venue(self):
        print("The venue is at Donald Trump Hall")
