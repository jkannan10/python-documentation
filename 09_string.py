# H   e   l   l   o  ,     W  o  r  l  d  !
# 0   1   2   3   4  5  6  7  8  9  10 11 12
#-13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1


val = "hello, world!"
x = len(val)
print(x)

# slicing string 

x = val[2:5] # 2 , 3 , 4
print(x)

x = val[2:] # from ind 2 to end
print(x)

x = val[:8] # from ind 0 to 7 
print(x)

x = val[-5:-2] # o r l
print(x)

# modification 
print(val.upper())
print(val.lower())
print(val.strip()) # like trim in java 
print(val.replace('h' , 'j'))
print(val.split(',')) # returns a list of string


#format 
val = 'Value to be inserted is {} {}'
print(val.format(10 , 20))

