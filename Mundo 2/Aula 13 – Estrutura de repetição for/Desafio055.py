'''Faça um programa que leia o peso de cinco pessoas
No final, mostre qual foi o maior e o menor peso lidos'''

a = 0
b = 0
for c in range(1, 6):
    peso = float(input('Peso em KG da {}ª pessoa: '.format(c)))
    if c == 1:
        a = peso
        b = peso
    else:
        if peso > a:
            a = peso
        elif peso < b:
            b = peso
print('Maior peso {}'.format(a))
print('Menor peso {}'.format(b))