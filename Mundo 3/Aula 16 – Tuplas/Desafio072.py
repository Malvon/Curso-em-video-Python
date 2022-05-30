'''Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso de zero até vinte
Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso'''


extenso = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', \
          'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', \
          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
n = int(input(('Digite um numero entre 0 e 20: ')))
while True:
    while n not in range(0, 21): #verifica se N esta entre 0 e 20
        n = int(input(('Tente novamente. Digite um numero entre 0 e 20: ')))
    print(f'Voce digitou o numero {extenso[n]}')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    while r not in 'SsNn':
        print('Invalido')
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'S':
        n = int(input(('Digite um numero entre 0 e 20: ')))
    else:
        print('Encerrado')
        break