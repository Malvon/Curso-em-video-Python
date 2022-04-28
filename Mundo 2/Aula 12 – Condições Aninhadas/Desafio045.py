'''Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Sua escolha: '))
if jogador > 2:
    print('\033[4mJOGADA INVALIDA!')
else:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!')
    sleep(0.5)
    print('Computador jogou \033[1:34m{}\033[m'.format(itens[computador]))
    print('Jogador jogou \033[1:34m{}\033[m'.format(itens[jogador]))
    if computador == 0:
        if jogador == 0:
            print('\033[1:33mEMPATE')
        elif jogador == 1:
            print('\033[1:32mJOGADOR VENCE')
        elif jogador == 2:
            print('\033[1:31mCOMPUTADOR VENCE')
    elif computador == 1:
        if jogador == 0:
            print('\033[1:31mCOMPUTADOR VENCE')
        elif jogador == 1:
            print('\033[1:33mEMPATE')
        elif jogador == 2:
            print('\033[1:32mJOGADOR VENCE')
    elif computador == 2:
        if jogador == 0:
            print('\033[1:32mJOGADOR VENCE')
        elif jogador == 1:
            print('\033[1:31mCOMPUTADOR VENCE')
        elif jogador == 2:
            print('\033[1:33mEMPATE')
