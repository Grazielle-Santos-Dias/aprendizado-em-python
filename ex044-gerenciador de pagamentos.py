print('{:=^40}'.format(' LOJAS DIAS '))
preço = float(input('Preço da Compra:  R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/pix
[2] à vista cartão de débito
[3] 2x cartão de crédito
[4] 3x ou mais no cartão de crédito''')
opção = float(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opção == 3:
    total = preço
    parcela = preço / 2
elif opção ==4:
    total = preço + (preço*20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2fCOM JUROS'.format(totparc, parcela))
print('Sua compra de R$ {:.2f}, vai custar R$ {:.2f} no final'.format(preço, total))



