from abc import ABC, abstractmethod

# Classe abstrata para expressões
class Expressao(ABC):
    @abstractmethod
    def interpretar(self):
        pass

# Expressão terminal para números
class Numero(Expressao):
    def __init__(self, valor):
        self.valor = valor

    def interpretar(self):
        return self.valor

# Expressão não terminal para soma
class Soma(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def interpretar(self):
        return self.esquerda.interpretar() + self.direita.interpretar()

# Expressão não terminal para subtração
class Subtracao(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def interpretar(self):
        return self.esquerda.interpretar() - self.direita.interpretar()

# Cliente
if __name__ == "__main__":
    # Representação da expressão: (10 + 5) - 3
    expressao = Subtracao(
        Soma(Numero(10), Numero(5)),
        Numero(3)
    )

    # Interpretar e exibir o resultado
    resultado = expressao.interpretar()
    print("Resultado da expressão:", resultado)  # Saída: Resultado da expressão: 12



#            Subtracao
#           /          \
#       Soma            Numero(3)
#      /    \
# Numero(10) Numero(5)
