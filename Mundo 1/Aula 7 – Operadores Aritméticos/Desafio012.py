'''Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto'''

n = float(input('Digite o preço do produto: R$'))
npre = n-(n*(5/100))
prazo = n+(n*(8/100))
print('O preço do produto para pagamento a vista é R${:.2f} e R${:.2f} para pagamento a prazo'.format(npre, prazo))