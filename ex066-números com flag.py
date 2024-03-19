num = soma = cont = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print(f'Foram digitados {cont} valores, e a soma entre eles é {soma}')
