
# IndexError	   --> When the wrong index of a list is retrieved.
# AssertionError --> It occurs when the assert statement fails
# AttributeError --> It occurs when an attribute assignment is failed.
# ImportError	   --> It occurs when an imported module is not found.
# KeyError	     --> It occurs when the key of the dictionary is not found.
# NameError      --> It occurs when the variable is not defined.
# MemoryError	   --> It occurs when a program runs out of memory.
# TypeError	     --> It occurs when a function and operation are applied in an incorrect type

# try : contains block of code that may cause exception
# except : contains a block of code which handles the exception
# else : excutes when there is no error occurs 
# finally : executes no matter what
# raise : used to throw an error manually
try:
  x = 5/0
except Exception:
  print("caught error" , Exception)
else :
  print('No error caught')
finally:
  print('hehehe')



