n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1+n2) / 2
print(' Tirando {:.1f} e {:.1f} , a média do aluno é {:.1f}'.format(n1, n2, media))
if media < 5:
    print('Você está REPROVADO')
elif media >= 7:
    print('Você está APROVADO')
else:
    print('Você está em RECUPERAÇÃO')

