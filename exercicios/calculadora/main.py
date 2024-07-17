from calculadora.calculadora import pegar_opcoes, mostrar_opcoes, calcular


def main():
    opcoes = pegar_opcoes()
    while True:
        mostrar_opcoes(opcoes)
        escolha = int(input("Escolha: "))
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        resultado = calcular(opcoes[escolha]['func'], numero1, numero2)
        print(resultado, '\n------------------------------')


"""
Define esse arquivo como um script executavel.
"""
if __name__ == "__main__":
    main()
