# sets é uma coleção que não possui objetos repetidos

lista = set([1,2,3,4,5,6,1,2,3,4])
print(lista)


nome = set("abacaxi")
print(nome)

linguagens = {"Python", "C", "C++", "Java", "Python"}
print(linguagens)

# Acessando dados, conjuntos não suportam indexação e nem fatiamento

numeros = {1,2,3,4,5,6,1,2,3,4}
numeros = list(numeros)

for indice, numero in enumerate(numeros):
        print(f"{indice}: {numero}")


conjunto_a = {1,2}
conjunto_b = {3,4}

uniao_conjuntos = conjunto_a.union(conjunto_b)
print(uniao_conjuntos)

conjunto_c = {1,2,3,4,5,6,1,2,3}
conjunto_d = {1,2,4}

print(conjunto_c.intersection(conjunto_d))

conjunto_e = {1,2,3,4,5,6}
conjunto_f = {1,2,3,4,7}

print(conjunto_e.difference(conjunto_f))
print(conjunto_f.difference(conjunto_e))

print(conjunto_e.symmetric_difference(conjunto_f))

print(conjunto_e.issuperset(conjunto_f))
print(conjunto_f.issuperset(conjunto_e))

conjunto_g = {1,2,3,4,5}
conjunto_h = {6,7,8,9}
conjunto_i = {1,0}

print(conjunto_g.isdisjoint(conjunto_h)) #se não tem intersseção
print(conjunto_g.isdisjoint(conjunto_i))

sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)
print(sorteio)

# print(sorteio.clear())

# sorteio.copy()

num = {1,2,3,4,5,6,7,8,9,0,1,2,3}
num.discard(1)
print(num)

# print(num.pop())
num.remove(9)
