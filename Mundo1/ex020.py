#DESAFIO 020: O mesmo professor do desafio anterior quer sortear a ordem da apresentação de trabalhos dos alunos. Faça um programa que leia o nome de quatro alunos e mostre a ordem sorteada.

import random

aluno1 = input('Primeiro aluno: ')
aluno2= input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print('A ordem de apresentação será')
print(lista)