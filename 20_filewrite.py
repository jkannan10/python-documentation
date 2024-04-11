try:
  f = open('demo1.txt' , 'w') # will over write the content
  f1 = open('demo.txt')
  for i in f1:
    f.write(i)
except FileNotFoundError:
  print("error")


try:
  f = open('demo1.txt' , 'a') # will append the content in the EOF
  f1 = open('demo.txt')
  f.write(f1.read())
except FileNotFoundError:
  print("Error")

