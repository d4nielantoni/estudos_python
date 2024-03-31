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

# .append = adicionar elementos na lista (um por um)
# .clear = limpar a lista
# .copy = copiar a lista em uma instância diferente
# .count = contar quantas vezes um elemento aparece na lista
# .extend = juntar listas

l2 = lista.copy()
print(lista)
print(id(l2), id(lista))
l2[0] = 2
print(l2)
print(lista)

cores = ['red', 'green', 'blue', 'orange', 'blue', 'blue','red']

print(cores.count("blue"))
print(cores.count("red"))
print(cores.count("orange"))

