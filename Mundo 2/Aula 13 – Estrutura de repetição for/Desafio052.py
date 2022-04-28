'''Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo'''

cont = 0
n = int(input('Numero: '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1:33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print('\n\033[mO numero {} foi divisivel \033[33m{}\033[m vezes'.format(n, cont))
if cont == 2:
    print('Por isso É PRIMO')
else:
    print('Por isso NAO É PRIMO')