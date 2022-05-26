'''Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).
No final, mostre a lista ordenada na tela'''


# valores = []
# for n in range(0, 5):
#     n = (int(input('Digite um valor: ')))
#     if len(valores) == 0:
#         valores.append(n)
#     for valor in valores:
#         if n > valor and n < valor+1:
#             valores.insert(valor, n)
# print(f'Os valores digitados em ordem foram {valores}')

#passo 1: criar lista
valores = []
#passo 2: recebeer valores
while len(valores) < 5:
    n = int(input('Digite um valor: '))
    if len(valores) == 0:
        valores.append(n)
#passo 3: comparar valor maior/menor
    for v in valores:
        if valores[v] < n < valores[v+1]:
            valores.insert(v, n)
        else:
            valores.append(n)
#passo 4: inserir valor na posicao correta


