# Listas

lista = [1,2,3,4,5,6,7,8]

print(lista[0])
print(lista[0:5])
print(lista[::-1]) #contrario
print(lista[-1]) #últinmo item
print(lista[2:])
print(lista[:2])

for numero in lista:
    if numero % 2 == 0:
        print(f"O numero {numero} é par")
    elif numero % 2 == 1:
        print(f"o numero {numero} é ímpar")


carros = ['Ford', 'Volvo', 'Mercedes']

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(indice, carro)


#Métodos da classe list

# .append = adicionar elementos na lista
# .clear = limpar a lista
# .copy = copiar a lista em uma instância diferente

