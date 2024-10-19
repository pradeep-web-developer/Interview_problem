# Encapsulation
# Modify the Car class to encapsulate the brand attribute,making it private, and provide a getter method for it.


# we are learning the project.
class Car:
  def __init__(self,userbrand,usermodel):
    self.__brand=userbrand
    self.model=usermodel
    
    
  def __get_brand(self):
    return self.brand +" !"
  
  def full_name(self):
    return f"{self.brand}{self.model}" # we are add the functionality.
  

  


class ElectricCar(Car):
  def __init__(self,brand,model,battery_size):
    super().__init__(brand,model)
    self.battery_size=battery_size

my_tesla = ElectricCar("Tesla ", "Model S","85kWh")
print(my_tesla.full_name())
print(my_tesla.get_brand())
