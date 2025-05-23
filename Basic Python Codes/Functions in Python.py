'''def hline():
    print(50*"=")

hline()
print("hello")

def sum(a,b):
    "This is sum"
    print("***")
    return (a+b)

a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
print("sum is ",sum(a,b))
print(type(a))

def add(num1, num2):
    "Add two numbers"
    num3=num1+num2
    return num3

num1=input("Enter No. :")
num2=input("Enter No. :")
ans=add(num1,num2)
print(f"The addition of {num1} and {num2} is {ans}")
print(type(add))
print(type(ans))


def present():
    print("welcome to school")
    a=input("enter the roll no.")
    print("Marked")

present()
'''
def multi(num1,num2)->int:
    "Multyplies two no."
    multi=num1*num2
    return multi