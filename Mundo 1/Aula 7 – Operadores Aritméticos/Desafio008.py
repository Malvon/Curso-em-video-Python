'''Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros'''

met = float(input('Digite um valor em metro(s): '))
print('{:.0f} metros é igual a {} milimetros '.format(met, met * 1000))
print('{:.0f} metros é igual a {} centimetros'.format(met, met * 100))
print('{:.0f} metros é igual a {} decimetros'.format(met, met * 10))
print('{:.0f} metros é igual a {} decametros'.format(met, met / 10))
print('{:.0f} metros é igual a {} hectometros'.format(met, met / 100))
print('{:.0f} metros é igual a {} kilometros'.format(met, met / 1000))