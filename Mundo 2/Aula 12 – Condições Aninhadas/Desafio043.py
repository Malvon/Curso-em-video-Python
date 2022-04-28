'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida'''

peso = float(input('Digite seu peso: Kg'))
altura = float(input('Digite sua altura: '))
IMC = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC < 25:
    print('Peso ideal')
elif IMC < 30:
    print('Sobrepeso')
elif IMC < 40:
    print('Obesidade')
else:
    print('Obesidade morbida')