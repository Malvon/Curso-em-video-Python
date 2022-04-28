'''Faça um programa que leia o sexo de uma pessoa
mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente
até ter um valor correto'''

sexo = ''
while 'F' != sexo != 'M':
    sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()[0]
    print('Digite sexo valido!')
print('Sexo {} registrado com sucesso'.format(sexo))