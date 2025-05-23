class calculation1: #parent class
    def sum(self,a,b):
        return a+b
class calculation2: #parent class
    def  sub(self,a,b):
        return a-b
class calculation3: #parent class
    def mul(self,a,b):
        return a*b
class calculation4: #parent class
    def div(self,a,b):
        return a/b
class derived(calculation1,calculation2,calculation3,calculation4): #child class
    pass
d=derived()
print(d.sum(10,20))
print(d.sub(30,20))
print(d.mul(40,60))
print(d.div(50,10))
print(d.sum(7,5))

