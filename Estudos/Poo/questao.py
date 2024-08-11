numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    if numero % 2 == 0:
        numeros.remove(numero)

print(numeros)

print(numeros.reverse())