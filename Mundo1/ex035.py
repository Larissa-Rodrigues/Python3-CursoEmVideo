#DESAFIO 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar triângulos.

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento: '))
segmento3 = float(input('Terceiro segmento: '))

soma12 = segmento1 + segmento2
soma13 = segmento1 + segmento3
soma23 = segmento2 + segmento3

if (segmento1 < soma23) and (segmento2 < soma13) and (segmento3 < soma12):
    print('Os segmentos acima PODEM FORMAR triângulo!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')