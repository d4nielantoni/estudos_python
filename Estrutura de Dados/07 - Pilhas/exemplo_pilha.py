class Pilha:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def remover(self):
        if not self.is_empty():
            return self.itens.pop()
        return None

    def topo(self):
        if not self.is_empty():
            return self.itens[-1]
        return None

    def is_empty(self):
        return len(self.itens) == 0

    def print_pilha(self):
        for item in reversed(self.itens): #reversed para imprimir a pilha na ordem certa
            print(item)

pilha = Pilha()
pilha.adicionar(1)
pilha.adicionar(2)
pilha.adicionar(3)

print(pilha.remover())
print(pilha.topo())
print(pilha.is_empty())

pilha.print_pilha()
