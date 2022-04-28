'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros'''

preco = float(input('Digite o valor do produto: R$'))
condicao = input('''Qual sera a forma de pagamento?
\033[4:34mDigite 1:\033[m dinheiro/cheque
\033[4:34mDigite 2:\033[m a vista no cartao
\033[4:34mDigite 3:\033[m 2x no cartao
\033[4:34mDigite 4:\033[m 3x ou mais no cartao
Sua escolha: ''')
if condicao == '1':
    preco = preco - preco * 0.10
    print('Tera um desconto de 10% e saira por R${:.2f}'.format(preco))
elif condicao == '2':
    preco = preco - preco * 0.05
    print('Tera um desconto de 5% e saira por R${:.2f}'.format(preco))
elif condicao == '3':
    preco = preco / 2
    print('Pagamento em 2x de R${:.2f}'.format(preco))
elif condicao == '4':
    preco = preco + preco * 0.20
    parcela = int(input('Em quantas vezes deseja parcelar? '))
    if parcela < 3:
        print('O minimo de parcelas é de 3x')
    else:
        print('Tera um acrescimo de 20% em {} parcelas de e saira por R${:.2f}'.format(parcela, preco / parcela))
else:
    print('Digite uma opcao valida')