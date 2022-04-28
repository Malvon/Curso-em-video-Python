'''Crie um programa que leia dois valores e mostre um menu
na tela:
1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''

n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))
esco = 0
while esco != 5:
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    esco = int(input('Sua escolha: '))
    if esco == 1:
        print('{} + {} = {}\n'.format(n1, n2, n1 + n2))
    elif esco == 2:
        print('{} x {} = {}\n'.format(n1, n2, n1 * n2))
    elif esco == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}\n'.format(n1, n2, n1))
        elif n1 < n2:
            print('Entre {} e {} o maior é {}\n'.format(n1, n2, n2))
        else:
            print('Os numeros sao iguais!\n')
    elif esco == 4:
        n1 = int(input('1º valor: '))
        n2 = int(input('2º valor: '))
    elif esco == 5:
        print('Finalizando o programa!')
    else:
        print('Numero invalido, tente novamente!\n')