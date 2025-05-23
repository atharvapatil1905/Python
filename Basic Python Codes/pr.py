class Student:
    def __init__(self, name, age):
        self.__name = name  # Private member
        self.__age = age    # Private member

    # Method to access private members
    def display_info(self):
        print(f"Student Name: {self.__name}")
        print(f"Student Age: {self.__age}")

    # Method to modify private members
    def update_info(self, name, age):
        self.__name = name
        self.__age = age
        print("Student information updated successfully!")

# Create an instance of the Student class
student = Student("Anagha", 16)

# Access private members directly (This will raise an error)
print("Attempting to Access Private Members Directly:")
try:
    print(student.__name)  # This will raise AttributeError
except AttributeError:
    print("Cannot access private member '__name' directly!")

# Access private members using class methods
print("\nAccessing Private Members via Method:")
student.display_info()

# Modify private members using a class method
print("\nUpdating Private Members via Method:")
student.update_info("Nandkishor", 17)

# Access the updated private members
print("\nAccessing Updated Private Members via Method:")
student.display_info()
