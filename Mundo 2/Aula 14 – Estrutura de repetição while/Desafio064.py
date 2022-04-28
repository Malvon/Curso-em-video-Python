'''Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada
No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag!)'''

n = soma = cont = 0
while n != 999:
    n = int(input('Digite um numero (999 encerra): '))
    if n != 999:
        cont += 1
        soma += n
print('\033[1:31mPrograma encerrado\033[m')
print('A soma dos numeros digitados foi \033[1:33m{}\033[m'.format(soma))
print('Foram digitados \033[1:33m{}\033[m numeros'.format(cont))