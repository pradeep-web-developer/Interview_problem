# Polymorphism.
# Question-: Demonstrate polymorphism by defining a method duel_type in both Car and ElectricCar classes, but with defferent behaviors.

class A:
  def show(self):
    print("Welcome")
    
  def show(self,firstname=''):
    print("Welcome",firstname)
    
  def show(self,firstname='',lastname=''):
    print("welcome",firstname,lastname)
    
obj=A()
obj.show()
obj.show('kiran')
obj.show('Kiran','kumari')