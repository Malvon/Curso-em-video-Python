'''Refaça o DESAFIO 35, dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:
- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes'''

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))
if l1 + l2 <= l3 or l2 + l3 <= l1 or l3 + l1 <= l2:
    print('Não é possivel obter um triangulo com essas medidas')
else:
    if l1 == l2 == l3:
        print('EQUILATERO')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('ISOCELES')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')