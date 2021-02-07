#DESAFIO 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no meio.

nome = input('Qual é seu nome completo? ').strip()

print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
