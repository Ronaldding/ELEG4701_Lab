class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

newCar = Car("Toyota", "Camry", 2022)
print("-----newCar-----")
print(newCar.make)
print(newCar.model)
print(newCar.year)

newCar2 = Car("Honda", "Accord", 2021)
print("-----newCar2-----")
print(newCar2.make)
print(newCar2.model)
print(newCar2.year)
print("---------------")