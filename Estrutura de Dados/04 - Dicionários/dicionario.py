# Classe dict
pessoa = {"nome": "Daniel", "idade":23}

# pessoa = dict(nome="Daniel", idade=23)

pessoa["nome"] = "Maria"
pessoa["telefone"] = "0123456789"
print(pessoa)

# Acessar dados de dicionário

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])


# Dicionários aninhados

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1111"},
    "daniel@gmail.com": {"nome": "Daniel", "telefone": "3333-2222"},
    "gabriel@gmail.com": {"nome": "Gabriel", "telefone": "3333-3333"},
    "lucas@gmail.com": {"nome": "Lucas", "telefone": "3333-4444"},
}


# Iterar Dicionários

for contato in contatos:
    print(contato, contatos[contato])


#Métodos classe dict

# clear = limpar dicionario
# copy = copia o dicionario (usado para nao mudar os dados do dicionario original)
# fromkeys = criar chaves do dicionário mas não atribuir valores, ou atribuir um valor padrão
# get = uma das formas de acessar valor no dicionário
# items = retorna lista de tuplas
# keys = retorna só a chaves do dicionário
# pop = remover uma chave do dicionário
#



