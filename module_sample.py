
# class with constructor and to string methods
class myClass:
  x = 5
  def __init__(self , x) -> None:
    self.x = x
  def add(self):
    return self.x + 5
  def __str__(self) -> str:
    return str(self.x)
  
sample = {
  'name':'jk',
  'age':20,
}
