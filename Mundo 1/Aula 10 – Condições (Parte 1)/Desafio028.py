'''n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
if m >= 6:
    print('Otima nota')
else:
    print('Tera que melhorar')'''

'''Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import choice
from time import sleep
lista = [0, 1, 2, 3, 4, 5]
n = choice(lista)
print('-' * 60)
print('Vou pensar em um numero de 0 a 5 e voce tera que adivinhar')
print('-' * 60)
num = int(input('Digite um valor: '))
print('PROCESSANDO...')
sleep(2)
if num > 5 or num < 0:
    print('Numero invalido, digite um numero de 0 a 5')
else:
    if num == n:
        print('Duas palavras: PARA BENS')
    else:
        print('Mais sorte na proxima, o numero era {}'.format(n))