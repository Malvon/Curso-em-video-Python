'''Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar
Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado'''

valor = float(input('Qual valor da casa? R$'))
sal = float(input('Qual seu salario? R$'))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao = valor / (anos * 12)
if sal * 0.3 <= prestacao:
    print('Não sera possivel prosseguir, emprestimo negado! Pois as parcelas seriam de \033[4:31mR${:.2f}\033[m'.format(prestacao))
else:
    print('Tudo certo! emprestimo liberado e o valor da parcela sera \033[4:36mR${:.2f}\033[m'.format(prestacao))