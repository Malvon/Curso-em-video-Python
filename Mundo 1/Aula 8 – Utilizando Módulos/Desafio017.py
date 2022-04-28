'''Faça um programa que leia o comprimento do cateto oposto (co)
e do cateto adjacente (ca) de um triângulo retângulo
calcule e mostre o comprimento da hipotenusa'''

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = ((ca*ca) + (co*co)) ** (1/2)
print('A hipotenusa dos numeros {} e {} é {:.2f}'.format(co, ca, hi))

#Segunda forma de como fazer
from math import hypot
co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))
hi = hypot(co, ca)
print("A hi dos números {} e {} é {:.2f}.".format(co, ca, hi))