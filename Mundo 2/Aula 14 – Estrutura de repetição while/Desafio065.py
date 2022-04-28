'''Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos
O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores'''

soma = cont = maior = menor = 0
r = 's'
while r == 's':
    num = float(input('Digite um numero: '))
    soma += num
    cont += 1
    if cont == 1:
        menor = maior = num
    else:
        if menor > num:
            menor = num
        elif maior < num:
            maior = num
    if r == 'n':
        print('Programa encerrado\n')
    r = str(input('Quer continuar? [S/N] ')).strip().lower()
media = soma / cont
print('O maior numero foi {}'.format(maior))
print('O menor numero foi {}'.format(menor))
print('Voce digitou {} numeros e a media dos valores foi {:.1f}'.format(cont, media))