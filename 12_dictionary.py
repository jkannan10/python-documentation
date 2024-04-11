x = {'name':"jk" , 'age':20}

print(x['name'])

x['dob'] = '15/03/2004'
print(x)
print(x.get('age'))
x.pop('dob')

print(x.keys())
print(x.values())
print(x.items())

# Looping through dictionary

for key in x:
  print('key' ,key , 'value' , x[key])
for i , j in x.items():
  print(i , j)

# Nested dictionary

x = {
   'y':{
     'name':'jk', 
     'age' :"20"
   },
   'z':{
     'id':21, 
     'city':'cbe'
   }
 }
for dic in x:
  for item in x[dic]:
    print(x[dic][item])