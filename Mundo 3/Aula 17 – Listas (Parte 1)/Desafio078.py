'''Faça um programa que leia 5 valores inteiros e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados
e as suas respectivas posições na lista'''


valores = []
maior = menor = 0
for cont in range(0, 5):         #lista com 5 elementos
    valores.append(int(input(f'Digite um valor para a posicao {cont+1}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print('-'*40)
print(f'Voce digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}.', end=' ')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}.', end=' ')
print()
