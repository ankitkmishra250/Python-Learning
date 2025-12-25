class Car:
    total_car_created = 0

    def __init__(self , name , brand , category):
        self.name = name 
        self.__brand = brand 
        self.category = category
        Car.total_car_created += 1
    
    def get_brand(self):
        return f"{self.__brand}  ! " 

class Electric_car():
    def turn_on_light(self):
        return "Light On"

class Fuel_car():
    def turn_on_engine(self):
        return "Turn On Engine"


class My_car(Car , Electric_car , Fuel_car):
   def __init__(self,name,brand,category):
        super().__init__(name,brand,category)


bmw = My_car("thar" ,"mahindra" , "fuel")

print(bmw.turn_on_engine())
print(bmw.turn_on_light())
print(bmw.get_brand())