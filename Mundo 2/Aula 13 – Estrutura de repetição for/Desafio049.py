''' Refaça o desafio 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for'''

n = int(input('Qual tabuada deseja saber? '))
print('A tabuada do {} é:'.format(n))
for c in range (1, 11):
    resultado = c * n
    print('{:2} X {:2} = {:3}'.format(n, c, resultado))