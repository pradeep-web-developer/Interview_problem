# we are learning the override program.
# whenever we writing method name with same signature in parent & child class called method overloading.

class A: # parent class
  def Disp(self):
    print("This is parent class method")

class B(A): #child
  def Disp(self):
    super().Disp()
    print("This is the child class")

obj=B()
obj.Disp()
    
  

