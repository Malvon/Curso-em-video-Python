'''Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
2 para hexadecimal'''

n = int(input('Digite um numero qualquer: '))
base = input('Qual sera base de conversão?\n'
             '[ 1 ] BINARIO\n'
             '[ 2 ] OCTAL\n'
             '[ 3 ] HEXADECIMAL\n'
             'Sua opção: ')
if base == '1':
    n1 = format(n, 'b')
    print('{} em binario é: {}'.format(n, n1))
elif base == '2':
    n1 = format(n, 'o')
    print('{} em octal é: {}'.format(n, n1))
elif base == '3':
    n1 = format(n, 'X')
    print('{} em hexadecimal é: {}'.format(n, n1))
else:
    print('Volte e digite uma base valida')