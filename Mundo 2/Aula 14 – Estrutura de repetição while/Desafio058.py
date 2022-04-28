'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer'''

cont = 0
from random import randint
from time import sleep
print('-' * 60)
print('Vou pensar em um numero de 1 a 10 e voce tera que adivinhar')
print('-' * 60)
num = int(input('Digite um valor de 1 a 10: '))
lista = randint(1, 10)
while num != lista:
    print('PROCESSANDO...')
    sleep(1)
    if num > 10 or num < 1:
        num = int(input('Numero invalido, digite um numero de 1 a 10: '))
    else:
        if num > lista:
            num = int(input('Tente um numero menor: '))
        elif num < lista:
            num = int(input('Tente um numero maior: '))
        cont += 1
print('Duas palavras: PARA BENS, e precisou de {} tentativas'.format(cont))

#Resolução do Guanabara
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero de 0 a 10')
print('Sera que voce consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas. Parabens!'.format(palpites))