from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ãngulo de {} tem o Seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(angulo, tangente))
