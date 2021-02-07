#DESAFIO 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Valor em metros: '))

centimetros = metros*100
milimetros = metros*1000

print('O valor em centimetros equivale a {}'.format(centimetros))
print('O valor em milimetros equivale a {}'.format(milimetros))