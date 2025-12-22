class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_name(self):
        return f"{self.brand} : {self.model}"
    
    def turn_on_light(self,swt=0):
        if swt == 0:
            print("Light Off")
        else:
            print("Light turned On")

my_car_01 = Car("Mercedies","GWagan")
my_car_02 = Car("toyota","Land Cruiser")
    
print(my_car_01.brand);
print(my_car_02.model)
print(my_car_02.display_name())
my_car_02.turn_on_light()