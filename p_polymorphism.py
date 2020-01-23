"""
Polymorphism involves using a single symbol or entity to represent multiple different types.
Python comprises of several ways to apply polymorphism:
    1. DuckTyping: It's a term used in dynamic programming that do not have strong typing. The idea is that
                    no type is need when invoking an exiting method on an object
    2. DuckTyping for Dependence Injection
    3. Operator Overloading
    4. Runtime Polymorphism


POLY = MULTI & MORPHIC = SHAPES | BEHAVIOUR
"""
class Duck:
    def talk(self):
        print("Quack Quack")

class Human:
    def talk(self):
        print("Hello")


#Duck Typing allows different methods to be passed into the callTalk() method
#The method dynamically detects which talk method to call.
#This is polymorphism since the same function can do multiple things depending on the obj passed
def callTalk(obj):
    obj.talk()

d=Duck()
callTalk(d)

h=Human()
callTalk(h)


#Dependency Injection involves injecting an object into another object
class Flight:
    def __init__(self,engine):
        self.engine=engine

    def startEngine(self):
        self.engine.start()

class AirBusEngine:
    def start(self):
        print("Starting Airbus Engine")

class BoingEngine:
    def start(self):
        print("Starting Boing Engine")


airbus = AirBusEngine()
boing = BoingEngine()
flg1 = Flight(airbus)
flg2 = Flight(boing)

flg1.startEngine()
flg2.startEngine()

""""Operator Overloading:
        The + operator is overloaded to perform multiply functions depending on the type of data
        been passed. For example passing numbers result in addition, passing strings result in
        concatenation, passing lists result in joining both list etc.
"""

""""Runtime Polymorphism:
        Aka dynamic method dispatch is a process in which a call to an overridden method is resolved
        at runtime rather than at compile-time. The determination of the object to be called is based
        on the object being referred to by the reference variable
"""
#In this example, toyota is used to represent both Car object and Bus object.
import o_inheritance as i

toyota=i.Car(True,"Camry",2018,897647)
print(toyota.model)
print(toyota.year)
print(toyota.vin)

toyota=i.Bus(True,"Haice",2014,457847)
print(toyota.model)
print(toyota.year)
print(toyota.vin)