'''Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro,
na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time da Chapecoense'''


ordem = 'Santos', 'Atletico-MG', 'Corinthians', 'Cuiaba', 'Internacional', \
        'Bragantino', 'Palmeiras', 'Flamengo', 'Coritiba', 'São Paulo', \
        'Botafogo', 'Fluminense', 'America-MG', 'Ceara', 'Avai', \
        'Athletico-PR', 'Atletico-GO', 'Goias', 'Juventude', 'Fortaleza'
print(f'Lista de times do Brasileirão 25/04/2022 {ordem}')
print('-'*90)
print(f'Os 5 primeiros são: {ordem[:5]}')
print('-'*90)
print(f'Os 4 ultimos são: {ordem[-4:]}')
print('-'*90)
print(f'Times em ordem alfabetica: {sorted(ordem)}')
print('-'*90)
print(f'Ceara esta em {ordem.index("Ceara")+1}º')