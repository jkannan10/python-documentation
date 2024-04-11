# function
def my_func(a):
  return a + 10
print(my_func(20))


# multiple args

def add(*param):
  return param[1] + param[0]
print(add(2 , 3))

# default value for param 

def sub (a = 2 , b = 3):
  return a- b
print(sub())
print(sub(5 , 9))
