'''Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses.
Seu aplicativo deverá analisar se a expressão passada
está com os parênteses abertos e fechados na ordem correta'''


expr = str(input('Digite uma expressao: '))
lista = []
for simbolo in expr:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()             #remove o ultimo elemento da lista
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressao valida!')
else:
    print('Expressao errada!')