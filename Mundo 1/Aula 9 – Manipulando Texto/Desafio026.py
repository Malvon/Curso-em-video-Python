'''Faça um programa que leia uma frase qualquer e mostre:
Quantas vezes aparece a letra "a"
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez'''

frase = str(input('Digite uma frase: ')).strip().lower()
a = frase.count('a')
b = frase.find('a')+1
c = frase.rfind('a')+1
print('A letra A aparece {} vezes\n'
      'A posicao da primeira letra A esta na casa {}\n'
      'A posicao da ultima letra A esta na casa {}'.format(a, b, c))