'''Crie um programa que tenha uma tupla com várias palavras
(não usar acentos).
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais'''


palavras = 'aprender', 'programar', 'linguagem', 'pyton', \
           'curso', 'gratis', 'estudar', 'praticar', \
           'trabalhar', 'mercado', 'programador', 'futuro'
for cont in palavras:
    print(f'\nNa palavra {cont.upper()} temos: ',end='')
    for letra in cont:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')


