class Calculadora:
    def soma(self, num1, num2):
        return num1 + num2

num1 = int(input())
num2 = int(input())

calc = Calculadora()

resultado = calc.soma(num1, num2)
print(resultado)
