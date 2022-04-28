'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1'''

print('-' * 40)
print('{:^38}'.format('BANCO CUEMVI'))
print('-' * 40)
n = int(input('Qual valor voce quer sacar? R$ '))
total = n
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-' * 40)
print('Volte sempre ao BANCO CUEMVI!')

#Outro modo de resolver
saque = int(input("Que valor você quer sacar? R$"))
notas = [50, 20, 10, 1]
cedulas = []
counter = 0
while saque > 0:
    for val in notas:
        cedulas.append(saque // val)
        saque = saque % val
        counter += 1
counter = 0
for item in cedulas:
    if item > 0:
        print(f"{item} cédulas de R${notas[counter]}")
    counter += 1 # teste
