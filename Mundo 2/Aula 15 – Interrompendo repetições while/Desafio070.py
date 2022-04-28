'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato'''

cont = soma = menor = 0
nome_menor = ''
print('-' * 30)
print('LOJA SUPER BARATAO')
print('-' * 30)
while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preco do produto: R$'))
    soma += preco
    if preco > 1000:
        cont += 1
    if menor == 0 or menor > preco:
        menor = preco
        nome_menor = nome
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        print('-' * 30)
    if r == 'N':
        break
print('{:-^50}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_menor} que custa R${menor:.2f}')