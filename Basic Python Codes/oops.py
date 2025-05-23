class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating objects (instances of the class)
person1 = Person("Anagha", 20)
person2 = Person("Nandkishor", 22)

# Accessing methods and attributes
person1.greet()
person2.greet()
