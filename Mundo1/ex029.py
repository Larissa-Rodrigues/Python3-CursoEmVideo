#DESAFIO 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')

else:
    excedente = (velocidade - 80) * 7
    print(f'MULTADO! Você excedeu o limite permite que é de 80 km/h.\nVocê deve pagar uma multa de R$ {excedente:.2f}!')
    print('Tenha um bom dia! Dirija com segurança!')