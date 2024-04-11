#In python the default user input is taken as string
#we need explitcilty convert them into the required type we want 

# user input 
x  = input()
print(x , type(x))

#typecasting of input to desired 

x = int(input())
print(x , type(x))

x = float(input())
print(x , type(x))

x = complex(input())
print(x , type(x))

x = bool(input())
print(x , type(x))
