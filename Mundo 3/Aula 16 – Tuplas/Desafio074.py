'''Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indique o menor e o maior valor que estão na tupla'''


from random import randint
ran = [randint(0, 10) for cont in range(5)]         #sorteia numeros com randint, limita a 5 numeros com o for
ran = tuple(ran)                                    #faz ran virar tupla
print(f'Valores sorteados: {ran}')
print(f'O maior valor sorteado foi {max(ran)}')
print(f'O menor valor sorteado foi {min(ran)}')