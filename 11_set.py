x = {"apple" , "orange" , "mango" , "apple"}
print(len(x) , x)
x.add("grapes")

for item in x:
  print(item , ' ' , end = ' ')

x.pop() # remove ;lastly add item
x.remove( "apple")
print(end = '\n')
print(x)