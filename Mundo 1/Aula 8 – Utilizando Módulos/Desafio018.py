'''Desafio 18: Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e tangente desse ângulo'''

from math import sin, cos, tan, radians
ang = int(input('Angulo: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('O seno é {:.2f} e cosseno é {:.2f} e a tangente é {:.2f}'.format(seno, coss, tang))