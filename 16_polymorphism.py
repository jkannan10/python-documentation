# polymorphism 
#unlike JAVA , pyhton does not support method over loading but we can do achiieve it by varible args 

class Vehicle:
  def __init__(self , name)->None:
    self.name = name
  def sound(self)->None:
    print("Generic class")
class car(Vehicle):
  def __init__(self , name , sound)->None:
    super().__init__(name)
    self.sound = sound
  def sound(self):
    print(self.sound)
class bike(Vehicle):
  def __init__(self, name , sound) -> None:
     super().__init__(name)
     self.sound = sound
  def sound(self):
    print(self.sound)


sample = car("bmw" , "tuk")
sample1 = bike("honda" , 'dur')

print(sample , sample1)

  