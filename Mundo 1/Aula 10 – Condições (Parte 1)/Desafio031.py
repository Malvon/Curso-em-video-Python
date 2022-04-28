'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas'''

distancia = float(input('Qual a distancia da viagem em Km? Km '))
if distancia <= 200:
    preco = distancia * 0.50
    print('O preço da passagem para {}Km custa R${:.2f}'.format(distancia, preco))
else:
    preco = distancia * 0.45
    print('O preco da passagem para {}Km custa R${:.2f}'.format(distancia, preco))