"""
Scenario: you need to model different types of vehicles using inheritance....
"""

class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, seats, type):
        self.seats = seats
        self.type = type
        super().__init__(brand, model, fuel_type)
    def start_engine(self):
        print(f"{self.brand} {self.model} is starting boom boom")

""" multiple inheritance like this"""

class ElectricCar(Car):
    def __init__(self, brand, model, fuel_type, seats, type, batteryCap):

        super().__init__(brand, model,"Electric", seats, type)
    def start_engine(self):
        print(f"{self.brand} {self.model} is silently powering up")

class Truck(Vehicle):
    def __init__(self, brand, model, fuel_type, MaxWeight):
        self.cargo_cap = MaxWeight
        super().__init__(brand, model, fuel_type)
    def start_engine(self): 
        print(f"{self.brand} {self.model} rumbles as the engine starts!")


My_car = Car("BMW", 2008, "gas", 5, "semi-automatic")
My_brother_car = ElectricCar("tesla", 2024, "electric", 4, "auto", 100000)
My_truck = Truck("Volvo", 2015, "Diesel", 20000)


My_car.start_engine()
My_brother_car.start_engine()
My_truck.start_engine()