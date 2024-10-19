# we are learning the in inherritance.
# Problem: Create an ElectricCar class that inherrits from the Car class and has an additional attribute battery-size.

class Car:
  def __init__(self,userbrand,usermodel):
    self.brand=userbrand
    self.model=usermodel
    
  def full_name(self):
    return f"{self.brand}{self.model}" # we are add the functionality.


class ElectricCar(Car):
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size=battery_size

my_tesla = ElectricCar("Tesla ", "Model S","85kWh")
print(my_tesla.full_name())

    
# my_car = Car("Scarpio ","Mahindra")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
     

# print(" Second Car Name ")
# my_new_car=Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)