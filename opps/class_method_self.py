# Add the method to the Car class that displayes the full name of the car(brand and model)

class Car:
  def __init__(self,userbrand,usermodel):
    self.brand=userbrand
    self.model=usermodel
    
  def full_name(self):
    return f"{self.brand}{self.model}" # we are add the functionality.
    
my_car = Car("Scarpio ","Mahindra")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())
     

print(" Second Car Name ")
my_new_car=Car("Tata","Safari")
print(my_new_car.brand)
print(my_new_car.model)