marathi=input("Enter Marks Of Marathi:")
maths=input("Enter Marks Of Maths:")
a=int(marathi)
b=int(maths)
if(a>50 and b>50 and a+b>100):
    print("You have Passed the Exam")
else:
    print("You have Failed In the Exam")