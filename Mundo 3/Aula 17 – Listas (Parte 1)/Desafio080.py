'''Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).
No final, mostre a lista ordenada na tela'''


valores = []
for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    if cont == 0 or n > valores[len(valores)-1]:    #lista[-1] tambem funciona
        valores.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):                   #varre a lista da primeira pos ate a ultima
            if n <= valores[pos]:                   #se o numero que quero inserir é menor que o numero em pos: insere
                valores.insert(pos, n)              #na posição pos insere n
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-'*60)
print(f'Os valores digitados em ordem foram {valores}')


