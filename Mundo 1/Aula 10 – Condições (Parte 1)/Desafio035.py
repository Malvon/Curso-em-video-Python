'''Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo
Inclusive posso dizer qual tipo de triângulo pode ser formado.
Não deve ser difícil isso em Python'''

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))
if l1 + l2 <= l3 or l2 + l3 <= l1 or l3 + l1 <= l2:
    print('Não é possivel um triangulo com essas medidas')
else:
    print('Um triangulo é possivel')
    if l1 == l2 and l2 == l3:
        print('Equilatero')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Isosceles')
    elif l1 != l2 or l2 != l3 or l3 != l1:
        print('Scaleno')