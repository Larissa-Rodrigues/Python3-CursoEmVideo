#DESAFIO 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = sqrt(cateto_oposto**2 + cateto_adjacente**2)
#Outra forma é importar a biblioteca math e depois inserir a linha de comando abaixo:
#hipotenusa = math.hypot(cateto_oposto, cateto_adjacente

print(f'A hipotenusa vai medir {hipotenusa:.2f}')

