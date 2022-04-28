'''Um professor quer sortear um dos seus quatro alunos
para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles
e escrevendo o do escolhido'''

#import random
#n = random.randint(1, 10)
#print(n)

from random import choice
n1 = input('1º aluno: ')
n2 = input('2º aluno: ')
n3 = input('3º aluno: ')
n4 = input('4º aluno: ')
lista = [n1, n2, n3, n4]
esco = choice(lista)
print('O aluno escolhido para apagar o quadro foi {}'.format(esco))