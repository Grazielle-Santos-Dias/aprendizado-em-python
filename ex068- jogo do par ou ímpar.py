from random import randint
print('-'*30)
print('Vamos jogar Par ou Ímpar')
print('-'*30)
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o Computador {computador}. Total de {total} ' ,end='')
    print('DEU PAR'if total % 2 == 0 else  ' DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 ==0:
            print('Você Venceu!')
            v = v + 1
        else:
            (print('Você Perdeu!'))
            break
    elif tipo == 'I':
        if total %2 == 1:
            print('Você Venceu!')
            v = v + 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f' GAME OVER! Você venceu {v} vezes.')
print('-'*30)


