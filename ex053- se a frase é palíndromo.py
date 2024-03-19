frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto [letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um \033[032mPalíndromo')
else:
    print( 'A frase digitada \033[031m Não é um Palíndromo!')

