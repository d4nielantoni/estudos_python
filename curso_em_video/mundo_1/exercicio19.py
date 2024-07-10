import random

alunos = []

for i in range(4):
    aluno = input('Digite o nome do aluno: ')
    alunos.append(aluno)

print(f'O aluno escolhido foi {random.choice(alunos)}')