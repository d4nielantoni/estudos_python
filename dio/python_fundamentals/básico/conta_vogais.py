def conta_vogais(texto):
    conta_vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú'}
    
    contador = 0
    
    for char in texto:
        if char in conta_vogais:
            contador += 1
        
    return contador

texto = input()

resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")