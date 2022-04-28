'''Faça um programa que leia um número de 0 a
9999 e mostre na tela cada um dos dígitos separados
ex.: digite um número: 1834
unidade: 4
dezenas: 3
centenas: 8
milhares: 1'''

n = int(input('Digite um numero de 0 a 9999: '))
uni = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10
mil = n // 1000 % 10
print('O numero digitado é: {}'.format(n))
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))