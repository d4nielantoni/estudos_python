def contar_caracteres(string):
    contador = {}
    
    for caractere in string:
        if caractere in contador:
            contador[caractere] += 1 
        else:
            contador[caractere] = 1 
    return contador

entrada = input().strip()
resultado = contar_caracteres(entrada)

print(resultado)
