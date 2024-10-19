class Car:
  def __init__(self,userbrand,usermodel):
    self.brand=userbrand
    self.model=usermodel
my_car = Car("Scarpio","Mahindra")
print(my_car.brand)
print(my_car.model)

print(" Second Car Name ")
my_new_car=Car("Tata","Safari")
print(my_new_car.brand)
print(my_new_car.model)