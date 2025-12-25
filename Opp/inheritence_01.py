class Car:
    def __init__(self , name , brand , category ):
        self.name = name 
        self.brand = brand 
        self.category = category 
    
    def print_details(self):
        return f"This is a {self.name}. \n Brand of this car is {self.brand}. \n This is a {self.category}"
    
    def engineStart(self , swt=0):
        if swt == 0:
            return "Engine Off ! Please Start The car"
        else :
            return  "Engine Is Start ! Enjoy the Ride "

class ElectricCar(Car):
    def __init__(self , name ,brand , category , price = "$300000"):
        super().__init__(name , brand , category)
        self.price = price
        
    def turn_on_racemode(self, swt = 0):
        if swt == 0 :
            return f"Turn on race mode"
        else:
            return f"Race Mode is on ! Enjoy Your Ride "
        
car = ElectricCar("Mahinda Suv 500" , "Mahindra " , "Eletric vehicle ");
print(car.engineStart(1))
print(car.turn_on_racemode(3))