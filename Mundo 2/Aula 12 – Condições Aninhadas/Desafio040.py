'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: reprovado
- média entre 5.0 e 6,9: recuperação
- média 7.0 ou superior: aprovado'''

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
if n1 > 10 or n2 > 10:
    print('Valor invalido!')
elif n1 < 0 or n2 < 0:
    print('Valor invalido!')
else:
    if m < 5:
        print('Nota {:.1f} \nREPROVADO!'.format(m))
    elif m >= 7:
        print('Nota {:.1f} \nAPROVADO!'.format(m))
    else:
        print('Nota {:.1f} \nRECUPERAÇÃO!'.format(m))