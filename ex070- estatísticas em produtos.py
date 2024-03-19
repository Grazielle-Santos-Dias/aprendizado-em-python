print('-='*10)
print('LOJA SUPER BARATÃO')
print('-='*10)
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont = cont + 1
    total = total + preço
    if preço > 1000:
        totmil = totmil + 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos mais de {totmil} produtos, custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')





