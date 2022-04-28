'''Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior; os dois são iguais'''

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print('O \033[4:36mprimeiro valor\033[m é maior')
elif n2 > n1:
    print('O \033[4:36msegundo valor\033[m é maior')
else:
    print('\033[4:33mNão existe\033[m valor maior, os dois sao \033[4:34miguais\033[m')