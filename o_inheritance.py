"""
    Inheritance is the process of defining an object from another object
"""

class Vehicle:

    def __init__(self,model,year,vin):
        self.model=model
        self.year=year
        self.vin=vin

    def start(self):
        print("Vehicle engine start")

class Car(Vehicle):

    def __init__(self, cruisecontrol, model, year, vin):
        #Vehicle.__init__(self,model, year, vin)
        super().__init__(model, year, vin)
        self.cruisecontrol=cruisecontrol

    def start(self):
        print("Car engine start")


class Bus(Vehicle):

    def __init__(self,auto, model, year, vin):
        #Vehicle.__init__(self,model, year, vin)
        super().__init__(model, year, vin)
        self.auto=auto

    def start(self):
        print("Bus engine start")
        



cr = Car(True,"Toyota Camry", 2018, 846783)

bu = Bus(False, "Toyota Haice", 2015, 513630)

print(cr.start)
print(bu.start())