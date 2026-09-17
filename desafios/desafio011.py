altura = float(input('Qual é a altura da parede? '))
largura = float(input('Qual é a largura da parede? '))
area = altura * largura
tinta = area / 2
print('A area da parede é {} m² e a quantidade de tinta necessária para pintar a parede é {} litros'.format(area, tinta))