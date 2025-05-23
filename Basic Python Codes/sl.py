alph=['a','b','c','d','e','f','g','h']
print(alph[1:4])
print(alph[::2])
print(alph[::-1])
print(alph[-5:-1:2])
alph[1:4]=[1,2,3]
print(alph)
alph[0:5]=["ram","ram","ram"]
print(alph)
alph=['a','b','c','d','e','f','g','h']
alph[len(alph):]=[1,2,3]
print(alph)

alph=['a','b','c','d','e','f','g','h']
alph[2:2]=['ram','seeta']
print(alph)


#sort the items of the list in place
mob=["3","6","8","7"]
print(mob)
mob.sort()
print(mob)

#return a shallow copy of the list
mob=["samsung","realme","redmi","apple"]
print(mob)
mob2=mob.copy()
print(mob2)


#search the list and find elements
mob=["samsung","realme","redmi","apple"]
print(mob)
print(mob.index("redmi"))
