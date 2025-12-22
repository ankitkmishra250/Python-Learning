class Car:
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model

my_car_1 = Car("Rolls Royce" , "Phantom")
my_car_2 = Car("Tata" , "Sierra")

print(my_car_1.brand)
print(my_car_1.model)
print(my_car_2.brand)
print(my_car_2.model)

class Fruits:
    def __init__(self, fruitsName , fruitsColor):
        self.fruitsName = fruitsName
        self.fruitsColor = fruitsColor

fruits_1 = Fruits("Mango" , "Green & Yellow")
fruits_2 = Fruits("Kiwi" , "Brown")

print(fruits_1.fruitsName)
print(fruits_2.fruitsColor)