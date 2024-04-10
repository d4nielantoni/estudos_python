# Listas
# Mutáveis, diferente das tuplas

list = [1,2,3,4,5,6,7,8]

print(list[0])
print(list[0:5])
print(list[::-1]) #contrario
print(list[-1]) #último item
print(list[2:])
print(list[:2])

for numero in list: #verificar se número é par ou ímpar
    if numero % 2 == 0:
        print(f"O numero {numero} é par")
    elif numero % 2 == 1:
        print(f"o numero {numero} é ímpar")


cars = ['Ford', 'Volvo', 'Mercedes']

for car in cars:
    print(car)

for indice, car in enumerate(cars):
    print(indice, car)


#Métodos da classe list

# .append = adicionar elementos na lista (um por um)
# .clear = limpar a lista
# .copy = copiar a lista em uma instância diferente
# .count = contar quantas vezes um elemento aparece na lista
# .extend = juntar listas
# .index = para saber o índice da primeira ocorrencia do objeto
# .pop = tira o última elemento por padrão, mas podemos passar o índice que queremos remover
# .remove = diferente do pop, aqui passamos o objeto que queremos remover
# .reverse = espelhar lista
# .sort = ordenar lista
# .len = ver tamanho da lista
# .sorted = ordenar iteráveis

l2 = list.copy()
print(list)
print(id(l2), id(list))
l2[0] = 2
print(l2)
print(list)

cores = ['red', 'green', 'blue', 'orange', 'blue', 'blue','red']

print(cores.count("blue"))
print(cores.count("red"))
print(cores.count("orange"))
print(cores.index("orange"))


new_list = [1,2,3,4,5,6]

for numbers in new_list:
    for i in range(3):
        print(numbers * i)






