entrada = input('Digite algo: ')

if entrada.isnumeric():
    print(f'O valor {entrada} é um número inteiro')
elif entrada.isalpha():
    print(f'O valor {entrada} é uma letra')
elif entrada.isalnum():
    print(f'O valor {entrada} é alfanumérico')
elif entrada.isspace():
    print(f'O valor {entrada} é ASCII')

