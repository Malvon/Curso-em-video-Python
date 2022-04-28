'''Crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre quantos dólares ela pode comprar'''

# Considere R$ 3.27 = US$ 1
n = float(input('Quantos reais tem na carteira? R$'))
dol = n/3.27
print('Com R${:.2f} voce pode comprar ${:.2f}'.format(n, dol))