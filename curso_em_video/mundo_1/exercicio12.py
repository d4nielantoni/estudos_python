preco_produto = float(input('Qual é o preço do produto? R$'))

desconto = preco_produto * 0.05

print(f'O produto que custava R${preco_produto:.2f}, na promoção com desconto de 5% vai custar R${preco_produto - desconto:.2f}')