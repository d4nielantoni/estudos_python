import math

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

hipotenusa_math = math.hypot(cateto_oposto, cateto_adjacente)

print(f'Sem utilizar math: {hipotenusa:.2f}')
print(f'Utilizando hypot: {hipotenusa_math:.2f}')