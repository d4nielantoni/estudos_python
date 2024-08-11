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

"""
Criando classes estudante agora
"""

class Estudante:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def caminhar(self):
        return 'Caminhando...'


estudante1 = Estudante("Daniel","Antoni")
estudante2 = Estudante("Gabriel","Antoni")

print(estudante1.nome, estudante1.sobrenome)
print(estudante2.nome, estudante2.sobrenome)
print(f"{estudante1.nome }" + estudante1.caminhar())

numeros = [1,2,3,4,5]
numeros = [num for num in numeros if num % 2]
print(numeros)


