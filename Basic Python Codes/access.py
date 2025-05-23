'''class Student:
    def __init__(self, name, age):
        self._name = name  # Protected member
        self._age = age    # Protected member

    def display_info(self):
        print(f"Student Name: {self._name}")
        print(f"Student Age: {self._age}")

# Create an instance of the Student class
student = Student("Anagha", 16)

# Access protected members directly (not recommended)
print("Student Name:", student._name)
print("Student Age:", student._age)

# Using class method to access protected members (recommended way)
#print("\nAccessing Protected Members via Method:")
#student.display_info()

# Modify protected members directly (not recommended)
#student._name = "Nandkishor"
#student._age = 17
#print("Student Name:", student._name)
#print("Student Age:", student._age

#
student._name="Raj"
student._age=23
print(f"Student name is {student._name} and his age is {student._age}.")'''

class Team:
    def __init__(self,name,roll):
         self._name= name
         self._roll= roll

    def display_info(self):
        print(f"Teammate:{self._name}")
        print(f"Teammate:{self._roll}")

team=Team("Athara","C")
#deleting Object


emp=Team()
emp.display()
del.emp()