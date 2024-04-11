#inheritance 

class parent:
  def __init__(self , name ,  age) -> None:
    self.name = name
    self.age = age
  def getName(self) -> str:
    return self.name
  def getAge(self)->int:
    return self.age
  def setName(self , name)->None:
    self.name = name
  def setAge(self , age)->None:
    self.age = age
  def __str__(self) -> str:
    return self.name +" "+ str(self.age)
  
class child(parent):
  def __init__(self, name, age , dept) -> None:
    super().__init__(name, age)
    self.dept = dept
  def __str__(self) -> str:
    return super().__str__()+" " + self.dept

sample = child("jk" , 20 , "IT")
print(sample)
sample.setAge(21)
print(sample)

