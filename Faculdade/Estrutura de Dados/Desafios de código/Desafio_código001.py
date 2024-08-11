# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input())
"""

 TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.  Se a quantidade de passos
for zero, imprima "Nenhum passo dado na floresta."
     Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.
"""


if quantidade_passos >= 1:
    for passo in range(quantidade_passos):
        if passo == 0: #os passos são contados a partir de 0, por isso que botei == 0 :)
            print(f"Explorador: {passo+1} passo")
        else:
            print(f"Explorador: {passo+1} passos")
else:
    print("Nenhum passo dado na floresta.")