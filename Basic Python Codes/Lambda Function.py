"""#Using Function
def double(x):
 	return x*2
print(double(5))
print(double(10))
# Same program Using Lambda function
double= lambda x: x*2
print(double(5))
print(double(25))

interest= lambda p,n,r : (p*n*r)/100
print(interest(10000,5,10))

greet=lambda name: print('Hello',name)
greet('Ramesh')

sum=lambda *x : x[0]+x[1]+x[2]+x[3]
print(sum(5,10,15,20))


#program to filter even numbers from a given list
li=[34,12,64,55,75,13,63]
elist=list(filter(lambda num: (num%2 ==0),li))
print(elist)

#Parameterless Lamdba Function
greet=lambda : print('Hello World !')
print(greet())

def myfunc(n):
    return lambda a:a*n

#mydb=myfunc(10)
mytp=myfunc(8)
#print(mydb(20))
print(mytp(14))

come=lambda name : print( "come in",name)
come("ramesh")

li=[4,8,9,0,5,7,77,78,35,42,90,65,94,23,25,48,49,69,67,]
ls=list(filter(lambda num:(num%3==0),li))
print(ls)"""

square=lambda p:p*p*p

print(square(3))