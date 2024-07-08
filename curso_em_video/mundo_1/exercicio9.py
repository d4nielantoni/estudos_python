numero_tabuada = input('Digite um número para ver a tabuada: ')

try:
    numero_tabuada = int(numero_tabuada)
    print(f'{numero_tabuada} x 1 = {numero_tabuada * 1}')
    print(f'{numero_tabuada} x 2 = {numero_tabuada * 2}')
    print(f'{numero_tabuada} x 3 = {numero_tabuada * 3}')
    print(f'{numero_tabuada} x 4 = {numero_tabuada * 4}')
    print(f'{numero_tabuada} x 5 = {numero_tabuada * 5}')
    print(f'{numero_tabuada} x 6 = {numero_tabuada * 6}')
    print(f'{numero_tabuada} x 7 = {numero_tabuada * 7}')
    print(f'{numero_tabuada} x 8 = {numero_tabuada * 8}')
    print(f'{numero_tabuada} x 9 = {numero_tabuada * 9}')
    print(f'{numero_tabuada} x 10 = {numero_tabuada * 10}')

except ValueError:
    print('Digite um número inteiro')