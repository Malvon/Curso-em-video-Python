'''Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos'''

cont = 0
media = 0
idadevelho = 0
nomevelho = ''
for c in range(1, 5):
    print('------- {}º PESSOA -------'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade
    if sexo == 'M':
        if c == 1:
            idadevelho = idade
            nomevelho = nome
        else:
            if idade > idadevelho:
                idadevelho = idade
                nomevelho = nome
    elif sexo == 'F':
        if idade < 20:
            cont += 1
print('A media de idade do grupo é de {:.0f} anos'.format(media/c))
print('O homem mais velho tem {} e chama {}'.format(idadevelho, nomevelho))
print(('Existem {} mulheres com menos de 20 anos'.format(cont)))