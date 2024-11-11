import random

def generate_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]

    for _ in range(2):
        soma = sum((len(cpf) + 1 - i) * v for i, v in enumerate(cpf))
        digito = 11 - soma % 11
        cpf.append(digito if digito < 10 else 0)

    return f"{''.join(map(str, cpf[:3]))}.{''.join(map(str, cpf[3:6]))}.{''.join(map(str, cpf[6:9]))}-{''.join(map(str, cpf[9:]))}"

print(generate_cpf())
