#DESAFIO 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Me diga um numero qualquer: '))

if numero % 2 == 0:
    print(f'O número {numero} é PAR!')

else:
    print(f'O número {numero} é ÍMPAR!')