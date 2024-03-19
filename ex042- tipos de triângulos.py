r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um Triângulo ',end='')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 and r3 != r2 and r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM formar um Triângulo')
# Equilátero = todos os lados iguais
# Isósceles = dois lados iguais e um diferente
# Escaleno = todos os lados diferentes