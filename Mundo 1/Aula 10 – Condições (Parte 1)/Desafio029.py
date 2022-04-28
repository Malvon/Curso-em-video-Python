'''Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite.'''

vel = int(input('Qual a velocidade do carro? Km/h '))
if vel > 80:
    print('Voce foi multado ')
    multa = 7 * (vel - 80)
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia e dirija com segurança')