'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou,
no final do jogo'''

from random import randint
cont = 0
r = ''
print('-=' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 15)
while True:
    n = int(input('Digite um valor: '))
    jogador = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print('-'*30)
    computador = randint(0, 5)
    total = n + computador
    if total % 2 == 0: #teste pra saber se é par
        r = 'PAR'
    else:
        r = 'IMPAR'
    print(f'Voce jogou {n} e o computador {computador}.\nTotal de {total} deu {r}')
    if jogador == 'P':
        if total % 2 == 0:
            cont += 1
            print('-' * 30)
            print('Voce VENCEU!!\nVamos jogar novamente...')
            print('-=' * 15)
        else:
            print('Voce perdeu!')
            print('-=' * 15)
            print(f'GAME OVER! Voce venceu {cont} vezes')
            break
    elif jogador == 'I':
        if total % 2 == 0:
            print('Voce perdeu!')
            print('-=' * 15)
            print(f'GAME OVER! Vitorias consecutivas: {cont}')
            break
        else:
            cont += 1
            print('-' * 30)
            print('Voce VENCEU!!\nVamos jogar novamente...')
            print('-=' * 15)
    else:
        print('Escolha invalida')
        break