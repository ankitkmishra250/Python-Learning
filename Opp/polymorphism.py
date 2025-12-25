class Car:
    def __init__(self , name , brand , category):
        self.name = name 
        self.__brand = brand 
        self.category = category
    
    def get_brand(self):
        return f"{self.__brand}  ! " 

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

toyota = Hybrid("Toyota Innova" , "toyota" , "hybrid car")
tesla = Electric_car("Tesla S Model" , "Tesla" , "Electric")
sierra = Fuel_car("Tata Sierra" , "Tata" ,"Fuel car")
print(toyota.recharging())
print(tesla.recharging())
print(sierra.recharging())