distancia = float(input('Qual a distãncia da viagem km/h?: '))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('O valor da sua passagem será de R$ {:.2f}'.format(preço))


