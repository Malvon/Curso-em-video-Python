'''Faça um programa que leia três números e
mostre qual é o maior e qual é o menor'''

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))
if n1 > n2 and n1 > n3:
    print('O maior numero foi {}'.format(n1))
elif n2 > n3:
    print('O maior numero foi {}'.format(n2))
else:
    print('O maior numero foi {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('O menor numero foi {}'.format(n1))
elif n2 < n3:
    print('O menor numero foi {}'.format(n2))
else:
    print('O menor numero foi {}'.format(n3))