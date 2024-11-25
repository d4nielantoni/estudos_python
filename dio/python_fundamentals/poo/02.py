class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def retornar_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

nome = input()
idade = int(input())

pessoa = Pessoa(nome, idade)

print(pessoa.retornar_informacoes())
