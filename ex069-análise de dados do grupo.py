print('-=' * 10)
print('CADASTRE UMA PESSOA')
print('-=' * 10)
tot18 = toth =  totm20 =  0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo? [M/F]:' )).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo? [M/F]:')).upper().strip()[0]
    if idade >= 18:
        tot18 = tot18 + 1
    if sexo == 'M':
        toth = toth + 1
    if sexo == 'F' and idade < 20:
        totm20 = totm20 +1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos : {tot18}')
print(f'Ao todo temos {toth} homens cadastrados.')
print(f'E temos {totm20} mulheres tem menos de 20 anos.')


