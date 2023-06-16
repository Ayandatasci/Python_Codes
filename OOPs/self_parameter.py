'''The self parameter is a reference to the current instance of the class, 
    and is used to access variables that belong to the class.'''

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

person = Person("Ayan")
person.greet()  # Output: Hello, my name is Ayan
