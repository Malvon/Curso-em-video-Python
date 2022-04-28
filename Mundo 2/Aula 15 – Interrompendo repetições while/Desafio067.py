'''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo'''


while True:
    n = int(input('Quer ver a tabuada de qual valor? (valor negativo encerra) '))
    print('-' * 40)
    if n < 0:
        print('Interrompido')
        break
    for cont in range(1, 11):
        resultado = n * cont
        print(f'{n:^3} X {cont:^3} = {resultado:^3}')
    print('-' * 40)
