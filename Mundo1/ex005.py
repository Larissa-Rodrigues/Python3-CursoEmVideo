#DESAFIO 005: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.

num = int(input('Digite um número: '))

sucessor = num + 1
antecessor = num - 1

print('O sucessor de {} é {}'.format(num, sucessor))
print('O antecessor de {} é {}'.format(num, antecessor))