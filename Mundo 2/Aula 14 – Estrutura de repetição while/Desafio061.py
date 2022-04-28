'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando
a estrutura while'''

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
ultimo = termo + (10 - 1) * razao
while termo <= ultimo:
    print(termo, end=' - ')
    termo += razao
print('FIM')