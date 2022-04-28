'''Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo'''

from datetime import date
sexo = int(input('''Qual seu sexo? 
[ 1 ] HOMEM
[ 2 ] MULHER
Sua escolha: '''))
if sexo == 1:
    ano = int(input('Informe o ano de nascimento: '))
    atual = date.today().year
    if ano >= atual:
        print('Ano invalido para a pesquisa')
    else:
        idade = atual - ano
        if idade < 18:
            tempo = 18 - idade
            print('Voce tem \033[1:36m{} anos\033[m e deve se alistar em \033[1:35m{} ano(s)\033[m'.format(idade, tempo))
            print('Seu alistamento sera em  \033[1:35m{}\033[m'.format(atual + tempo))
        elif idade == 18:
            print('Voce ja tem \033[1:36m{} anos\033[m e esta na hora de se alistar!'.format(idade))
        else:
            tempo = idade - 18
            print('Voce tem \033[1:36m{} anos\033[m e esta \033[1:31m{} ano(s)\033[m atrasado de se alistar!'.format(idade, tempo))
            print('Seu alistamento foi em \033[4:31m{}\033[m'.format(atual - tempo))
elif sexo == 2:
    print('\033[4:33mVoce nao precisa se alistar!\033[m')
else:
    print('Digite uma opcao valida')