'''Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento'''

sal = float(input('Digite o salario R$'))
nsal = sal+(sal*15/100)
print('O novo salario com 15% de aumento sera de {:.2f}'.format(nsal))