#DESAFIO 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse Ângulo.

from math import radians, sin, cos

angulo = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = seno/cosseno

print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')