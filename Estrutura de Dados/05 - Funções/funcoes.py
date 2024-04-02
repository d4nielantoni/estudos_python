"""
Funções: bloco de código que pode receber uma lista de parâmetro

Usar as funções torna o código mais legível e possibilita o reaproveitamento do código
"""

def hello():
    print("Hello World!!")

def hello2(name):
    print(f"Hello {name}")

def hello3(name="Daniel"):
    print(f"Hello {name}")

hello()
hello2(name="Daniel")
hello3()

def total_sum(numbers):
    return sum(numbers)

print(total_sum([1,2,3,4])) #10


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(retorna_antecessor_e_sucessor(2)) #(1, 3)


def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Palio","FIAT", "1999", "ABC-1234")

"""
Args e kwargs

*args: renderiza como uma tupla e **kwargs: renderiza como dicionário
"""

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados= "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Sexta-Feira 25 de Agosto de 2024","asdads", "dadadasd")