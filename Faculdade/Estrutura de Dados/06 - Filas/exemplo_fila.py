class Fila:
    def __init__(self):
        self.itens = []

    def adicionar_elemento(self, item):
        self.itens.append(item)

    def remover_elemento(self):
        if not self.is_empty():
            return self.itens.pop(0)
        return None

    def frente(self):
        if not self.is_empty():
            return self.itens[0]
        return None

    def is_empty(self):
        return len(self.itens) == 0

    def print_fila(self):
        for item in self.itens:
            print(item)

fila = Fila()
fila.adicionar_elemento(1)
fila.adicionar_elemento(2)
fila.adicionar_elemento(3)
fila.adicionar_elemento(4)
print(fila.remover_elemento())
print(fila.frente())
print(fila.is_empty())
 
fila.print_fila()
