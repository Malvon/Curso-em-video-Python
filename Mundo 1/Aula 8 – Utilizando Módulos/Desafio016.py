'''from math import sqrt
n = int(input('Digite um valor: '))
raiz = sqrt(n)
print('A raiz de {} é igual a {:.2f} '.format(n, raiz))

import emoji
print(emoji.emojize('Ola mundo :earth_americas:', use_aliases=True))'''

'''Crie um programa que leia um número real qualquer pelo teclado
e mostre na tela a sua porção inteira'''

from math import trunc
n = float(input('Digite um valor real: '))
n = trunc(n)
print(n)