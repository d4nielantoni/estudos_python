"""
Como criar classes em Python, chamar métodos e etc

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce_yourself(self):
        return ("My name is " + self.name + ". And I am " + str(self.age) + " years old")

    def walk(self):
        return ("I am walking")

Person = Person('Daniel', 23)

print(Person.name)
print(Person.age)
print(Person.introduce_yourself())
print(Person.walk())

