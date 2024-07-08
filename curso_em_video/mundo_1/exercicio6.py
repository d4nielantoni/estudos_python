numero = input('Digite um número: ')

try:
    numero = int(numero)
    dobro = numero * 2
    triplo = numero * 3
    raiz = numero ** (1/2)

    print(f'O dobro de {numero} é {dobro}, o triplo é {triplo} e a raiz quadrada é {raiz}')

except ValueError:
    print('Digite um número inteiro')