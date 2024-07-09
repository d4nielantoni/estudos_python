altura_parede = float(input('Digite a altura da parede: '))
largura_parede = float(input('Digite a largura da parede: '))

area_parede = altura_parede * largura_parede

litros_tinta = area_parede / 2

print(f'Para pintar uma parede de {area_parede:.2f}m², você precisará de {litros_tinta:.2f}L de tinta.')