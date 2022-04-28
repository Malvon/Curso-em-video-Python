'''Crie um programa que leia o nome de uma cidade e diga
se ela começa ou não com a palavra "Santo"'''

nome = input('Nome da cidade: ').strip().lower().split()
print(nome[0] == 'santo')