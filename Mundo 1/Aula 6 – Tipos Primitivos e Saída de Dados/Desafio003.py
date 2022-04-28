'''Crie um script Python que leia dois números
e tente mostrar a soma entre eles'''

num1 = int(input("Primeiro número: \n"))
num2 = int(input("Segundo número: \n"))
print("A soma é:", num1 + num2)
print("A soma é: %d!" % (num1 + num2))
print("A soma é: {}!".format(num1 + num2))

# Os três formatos de print aceitam operações entre variáveis

n1 = int(input('Digite um numero '))
n2 = int(input('Digite outro numero '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))