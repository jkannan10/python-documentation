i = 1
while i < 6:
  print (i , ' ' , end = '')
  i += 1

print()
i = 1
while i < 6:
  if i == 3:
    i += 1
    continue
  print(i , ' ' , end = '')
  if i == 4:
    break
  i += 1
print()
#we can include a optional else block when we use while or for and it will execute only when loop condition fails

i = 1
while i < 6:
  print(i , ' ' , end = '')
  i += 1
else :
  print("End of While" , i)



# For loop

for i in range(6):
  print(i , ' ' , end = '')
print()

x = "apple"

for i in range(len(x)):
  print(x[i] , ' ' , end = '')

x = ["apple" , "banana" , "grapes" , 'orange']
print()
for i in x:
  print(i , ' ' , end = '');
print()
for i in range (2 , 11 , 2): # range( start , end , steps )
  print(i , ' ' , end = '')
#Optional else block is also available for 'for Loop '
