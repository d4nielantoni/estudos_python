import math

numero = float(input('Digite um número: '))
print(f'O número digitado foi {numero} e a sua porção inteira é {math.trunc(numero)}')

# The math.trunc() function returns the integer part of a number by removing the fractional digits.