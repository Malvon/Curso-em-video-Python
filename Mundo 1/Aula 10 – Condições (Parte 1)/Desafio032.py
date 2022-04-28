'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO'''

from datetime import date
ano = int(input('Ano: '))
if ano == 0:
    ano = date.today().year #pega data atual do computador
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Bissexto')
else:
    print('Nao é bissexto')