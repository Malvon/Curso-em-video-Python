'''Faça um programa que leia um número qualquer e mostre
o seu fatorial
exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120'''

n = int(input('Quer saber fatorial de qual numero? '))
fat = n
while n != 1:
    n -= 1
    fat *= n
print('O fatorial do numero escolhido é {}'.format(fat))