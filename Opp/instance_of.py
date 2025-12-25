class Car:
    total_car_created = 0

    def __init__(self , name , brand , category):
        self.name = name 
        self.__brand = brand 
        self.category = category
        Car.total_car_created += 1
    
    def get_brand(self):
        return f"{self.__brand}  ! " 
    
    @staticmethod
    def car_description():
        return "Car is a transport medium"

class Electric_car(Car):
    def __init__(self ,name , brand , category):
        super().__init__(name , brand , category)

    def recharging(self):
        return "recharging through Eletricity"

class Fuel_car(Car):
    def __init__(self , name , brand , category):
        super().__init__(name , brand , category)
    
    def recharging(self):
        return "recharging through fuel"

class Hybrid(Car):
    def __init__(self , name , brand , category):
        super().__init__(name , brand , category)
    
    def recharging(self):
        return "recharging through both(feuls and electricity)"

print(Car.car_description())

toyota = Hybrid("Toyota Innova" , "toyota" , "hybrid car")
print(isinstance(toyota , Car))
print(isinstance(toyota , Electric_car))
print(isinstance(toyota , Hybrid))