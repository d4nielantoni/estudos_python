"""
Aqui é onde fica as operações disponiveis na calculadora,
- func: a função lambda
- operacao: nome da operação
"""
def pegar_opcoes():
    return [
        {"func": lambda val1, val2: val1 + val2, "operacao": "Soma"},
        {"func": lambda val1, val2: val1 - val2, "operacao": "Subtração"},
        {"func": lambda val1, val2: val1 * val2, "operacao": "Multiplicação"},
        {"func": lambda val1, val2: val1 / val2, "operacao": "Divisão"},
    ]

"""
Aqui será printado na tela as opções disponiveis
i: numero da opcao
opcao[i][operacao]: retorna o nome da operacao tendo em vista o numero.
"""
def mostrar_opcoes(opcoes):
    for i in range(len(opcoes)):
        print(i, " - ", opcoes[i]['operacao'])


"""
Calcula o resultado
func: A operação que será aplicada
val1, val2: os valores a serem aplicados
"""
def calcular(func, valor1, valor2):
    print(func(valor1, valor2))
    return func(valor1, valor2)
