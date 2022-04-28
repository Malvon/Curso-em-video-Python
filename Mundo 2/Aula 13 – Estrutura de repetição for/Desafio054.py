'''Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''

from datetime import date
atual = date.today().year
cont1 = 0
cont2 = 0
for c in range(1, 8):
    ano = int(input('Ano de nascimento {} pessoa: '.format(c)))
    if ano > atual:
        print('INVALIDO')
    else:
        if atual - ano >= 21:
            cont1 += +1
        else:
            cont2 += +1
print('{} pessoas ja atingiram maioridade'.format(cont1))
print('{} ainda nao atingiram maioridade'.format(cont2))