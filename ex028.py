#DESAFIO 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário ganhou ou perdeu.

from random import randint
computador = randint(0,5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
usuario = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')

if usuario == computador:
    print('PARABÉNS! Você conseguiu me vencer!')

else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {usuario}!')