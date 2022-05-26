'''Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla.
No final, mostre:
a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
c) quais foram os números pares'''


numero = (int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')))
print(f'Voce digitou os valores: {numero}')
print(f'O numero 9 apareceu {numero.count(9)} vezes')
if 3 not in numero:
    print(f'O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {numero.index(3)+1}ª posição')
print('Os valores pares digitados foram: ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')