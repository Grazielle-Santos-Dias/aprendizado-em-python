salário = float(input('Informe o salário do funcionário:R$ '))
novosalário = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f} '.format(salário, novosalário))
