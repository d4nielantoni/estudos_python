km_percorridos = float(input('Quantos km foram percorridos? '))
dias_alugado = int(input('Por quantos dias o carro foi alugado? '))

preco = (60 * dias_alugado) + (0.15 * km_percorridos)

print(f'O total a pagar é de R${preco:.2f}')