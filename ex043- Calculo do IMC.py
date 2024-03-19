peso = float(input('Informe seu peso Kg: '))
altura = float(input('Informe a sua altura (m): '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print("Você está abaixo do peso ideal")
elif imc <= 25:
    print('Você está no peso ideal')
elif imc <= 30:
    print('Você está com sobrepeso')
elif imc <= 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')
