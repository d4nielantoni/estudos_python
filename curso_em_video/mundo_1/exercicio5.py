numero = input('Digite um número: ')

try:
    numero = int(numero)
    antecessor = numero - 1
    sucessor = numero + 1

    print(f'O antecessor de {numero} é {antecessor} e o sucessor é {sucessor}')
except ValueError:
    print('Digite um número inteiro')
