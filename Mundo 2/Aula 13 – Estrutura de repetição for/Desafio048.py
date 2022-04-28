'''Faça um programa que calcule a soma entre
todos os números impares que são múltiplos de
três (3) e que se encontram no intervalo de 1 até 500'''

s = 0
c = 0
for n in range (1, 501):
    if n % 2 == 1 and n % 3 == 0:
        s += n
        c += 1
print('A soma entre {} os impares multiplo de 3 entre 1 e 500 é \033[1:33m{}\033[m'.format(c, s))