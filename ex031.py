#DESAFIO 031: Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia:.1f} km.')

if distancia <= 200:
    preco = 0.5 * distancia

else:
    preco = 0.45 * distancia

#Outra forma de resolver a condição é:
#preco = 0.5 * distancia if distancia <= 200 else preco = 0.45 * distancia

print(f'E o preço da sua passagem será de R$ {preco:.2f}')