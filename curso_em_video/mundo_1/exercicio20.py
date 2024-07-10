import random

alunos = []

for i in range(4):
    aluno = input('Digite o nome do aluno: ')
    alunos.append(aluno)    

print(f'A ordem de apresentação será: {random.sample(alunos, 4)}') #random.sample() retorna uma lista com os elementos embaralhados