'''Crie um script Python que leia o nome de uma pessoa e mostre
uma mensagem de boas-vindas de acordo com o valor digitado'''

entrada = input("Digite seu nome: \n")
print("\033[1:33:40mOlá, {}! Prazer em conhecer você!\033[m".format(entrada))

'''Crie um programa que escreva "Olá, mundo" na tela'''

print("\033[1:31:40mOlá, mundo!\033[m")
msg = "\033[7:40mHello, world!\033[m"
print(msg)