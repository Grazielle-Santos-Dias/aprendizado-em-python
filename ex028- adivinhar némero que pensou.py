from random import randint
from time import sleep
computador = randint(0, 5)# Faz o computador "PENSAR"
print('Vou pensar em um número entre 0 e 5.Tente adivinhar...')
print('-----'*20)
jogador = int(input('Em que número eu pensei? '))# jogador tenta adivinhar
print('Processando...')
sleep(2)
if jogador == computador:
    print('Parabéns! você conseguiu me vencer')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador,jogador))







