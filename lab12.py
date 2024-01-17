"""
Title: Car Class.
Author: Jon Burstein
Details: This is a python progam that contains a class called auto that can be used
to create cars. It teaches how classes work.
"""

class Auto:

    def __init__(self):
        self.model = 'NONE'
        self.miles = 0
        self.gas = 0
    
    def set_model(self,model):
       self.model = model

    def set_miles(self,miles):
        self.miles = int(miles)
    
    def set_gas(self,gas):
        self.gas = float(gas)
    
    def miles_driven(self):
        return float(self.miles / self.gas)

my_car = Auto()
my_car.set_model("Toyota Camry")
my_car.set_miles(100)
my_car.set_gas(10)

print(f"A {my_car.model} was driven {my_car.miles} miles and used {my_car.gas} "
      f"gallons of gas, and gets {my_car.miles_driven()} mpg.")