'''A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 20 anos: sênior
acima de 20: master'''

from datetime import datetime
nasc = int(input('Ano de nascimento do atleta: '))
atual = datetime.now().year
idade = atual - nasc
if idade <= 9:
    print('O atleta tem {} anos e é MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e é INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e é JUNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e é SENIOR'.format(idade))
else:
    print('O atleta tem {} anos e é MASTER'.format(idade))