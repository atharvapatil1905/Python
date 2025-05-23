
    class Employee:
        #constructor
        def __init__(self,name,salary,project):
        #data members
        self.name=name
        self.salary=salary
        self.project=project

    #method to dispaly employees details
    def show(self):
        print("Name: ",self.name,"Salary:",self.salary)

    #method to disipaly employee project
    def work(self):
        print(self.name, 'is working on ',self.project)

#creating object of a class
emp1 = Employee('Mahesh',15000,'South Project')
emp2= Employee('Rajesh', 25000,'Sales Project')
#calling public method of the class
emp1.show()
emp2.show()
emp1.work()
emp2.work()
