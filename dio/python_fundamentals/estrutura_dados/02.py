def elementos_comuns(lista1, lista2):
    """
    Recebe duas listas de números inteiros como strings e retorna os elementos comuns como uma lista de inteiros.
    """
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    return list(set1.intersection(set2))

lista1 = input().split()
lista2 = input().split()

if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")
