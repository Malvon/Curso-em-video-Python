'''Faça um programa que leia a largura e a algura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2m²'''

lar = float(input('Qual a largura da parede em metros? '))
alt = float(input('Qual a altura da parede em metros? '))
area = lar * alt
print('A area da parede é de {} m²'.format(area))
tin = area/2
print('Serão necessarios {} litros de tinta'.format(tin))