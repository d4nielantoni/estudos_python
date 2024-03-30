
print(
    """
    =========== MENU ==========
    
    [1] Adicionar
    [2] Subtrair
    [3] Multiplicar
    [4] Dividir
    
    ===========================
    """
)
escolha = int(input("Escolha: "))

if escolha == 1:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    soma = numero1 + numero2
    print(f"{numero1} + {numero2} = {soma}")

elif escolha == 2:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    subtracao = numero1 - numero2
    print(f"{numero1} - {numero2} = {subtracao}")

elif escolha == 3:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    multiplicacao = numero1 * numero2
    print(f"{numero1} * {numero2} = {multiplicacao}")

elif escolha == 4:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    divisao = numero1 / numero2
    print(f"{numero1} / {numero2} = {divisao}")

