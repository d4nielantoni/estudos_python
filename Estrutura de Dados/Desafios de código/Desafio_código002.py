
itens = []

for i in range(3):
    item = input("Informe o item: ")
    itens.append(item)

print("Lista de itens:")
for item in itens:
    print(f"- {item}")