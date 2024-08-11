capacidade_atual, aumento_percentual = map(int, input().split())

nova_capacidade_total = capacidade_atual * (1 + aumento_percentual / 100)

print(int(nova_capacidade_total))