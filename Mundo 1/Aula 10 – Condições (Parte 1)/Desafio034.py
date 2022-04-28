'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de R$ 15%.'''

sal = float(input('Salario do funcionario: R$'))
if sal >= 1250:
    nsal = sal + sal * 0.10
else:
    nsal = sal + sal * 0.15
print("O salario de R${:.2f} foi para R${:.2f}".format(sal, nsal))