'''Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão'''

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
ultimo = termo + (10 - 1) * razao
for i in range(termo, ultimo + razao, razao):
    print(i, end=' - ')
print('ACABOU')