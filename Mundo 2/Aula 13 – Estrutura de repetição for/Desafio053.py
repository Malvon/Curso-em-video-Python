'''Crie um programa que leia uma frase qualquer
E diga se ela é um palíndromo, desconsiderando os espaços
Após a sopa
A sacada da casa
A torre da derrota
o lobo ama o bolo
Anotaram a data da maratona'''


frase = str(input('Digite alguma frase: ')).strip().upper().split()
junto = ''.join(frase)
inverso = junto[::-1] #tirar essa linha para funcionar o que ta entre aspas
'''inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao é um palindromo')