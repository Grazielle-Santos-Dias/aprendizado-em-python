times = ('Corinthians', 'Palmeiras','Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí',  'Ponte Preta', 'Atlético- GO')
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos colocados são: {times[16:20]}')
print('-='*15)
print(f' Times em Ordem Alfabética: {sorted(times)}')
print('-='*15)
print(f'O Chapecoense está na {times.index("Chapecoense") +1 }ª posição')


