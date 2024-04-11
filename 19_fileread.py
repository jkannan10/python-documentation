try:
  f = open("demo.txt")
  print(f.read()) # read all the content
except FileNotFoundError:
  print("Error")

try:
  f = open("demo.txt")
  print(f.readline()) # read only one line
except FileNotFoundError:
  print("Error")

try:
  f = open("demo.txt")
  for i in f :
    print(i) # read one line for each iteration
except Exception:
  print("Error")


# when the file doesnot exits it will throw an error
# file defaultly open in read mode with "t"-> text
