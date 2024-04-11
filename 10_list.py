x = ["apple" , "banana" , "grapes" , "orange" , "pomo" , "watermelon" , "kiwi"] #  x = list(("a"  'b' , 'c'))

# Access
print(x , len(x))
print(x[0]) # first
print(x[-1]) # last
print(x[2:5]) # splice 
print("apple" in x)

# Modification 
x[1] = 'cherry' 
x.insert(len(x) ,'jk')
x.append('last') # add at last
x.pop() # remove at last or at index
x.remove('jk') # removes value 
del x[5] # remove at ind
print(x)

# Iteration 
for fruit in x :
  print(fruit , end = ' ')
print()
for i in range(len(x)):
  print(i , end = ' ')

# Sorting 
print(x.sort())
print(x.sort(reverse = True))

# List Comprehension

newList = [i  for i in x if "a" in i] # It is like map
print(newList)