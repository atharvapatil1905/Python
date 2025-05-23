#changing add adding dictionary elements
emp={'name':'Ram','age':31}
print(emp)

#update value
emp['age']=21
print(emp)

#add item
emp['address']='Pune'
print(emp)
print(emp.keys())

#removeing particular items, return its value
print(emp.pop('address'))
print(emp)


#remove an arbitrary item return key, value
print(emp.popitem())
print(emp)


emp1={'name':'Ram','age':31}
print(emp1)

emp1.popitem()
print(emp1)

item1 = {'wadapav': 25, 'misal': 70, 'pasta': 100, 'burger': 120, 'tea': 10, 'coffi': 20}
print("Welcome to the restaurant!")
print("Here is the menu:")
for key, value in item1.items():
   print(f"{key:<10} {value:<20}")

#{value:<20}

materials={'wood':10000,'cement':4500,'steel':67000}
print("This is the material list")
for key,value in materials.items():
    print(f"{key:<20}{value:>10}")