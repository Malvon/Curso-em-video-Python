'''Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista'''


valores = []
cont = 1
resp = ''
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'S':
        cont += 1
    elif resp == 'N':
        print('-'*40)
        print(f'Voce digitou {cont} elementos')
        valores.sort(reverse=True)
        print(f'Os valores em ordem decrescente são {valores}')
        if 5 in valores:
            print('O valor 5 faz parte da lista!')
        else:
            print('O valor 5 não faz parte da lista!')
        break
# #
# # passo 1 criar lista
# valores = []
# cont = 0
# # passo 2 incluri valores
# while True:
#     valores.append(int(input('Digite um valor: ')))
#     cont += 1
#     resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#     if resp == 'S':
#         continue
#     else:
#         break
# # passo 3 saber quantos foram dig
# print(f'Voce digitou {cont} valores')
#
# # passo 4 ordenar lista de forma decescente
# valores.sort(reverse=True)
# print(f'Os valores em ordem decescente sao {valores}')
#
#
# # passo 5 se valor 5 foi dig e esta ou nao na list
# if 5 in valores:
#     print('O valor 5 faz parte da lista!')
# else:
#     print('O valor 5 nao faz parte da lista!')