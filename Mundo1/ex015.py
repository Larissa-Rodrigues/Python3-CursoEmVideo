#DESAFIO 015: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

dias_alugados = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km rodados? '))

valor = dias_alugados * 60 + 0.15 * km_rodados

msg = f'O total a pagar é de R$ {valor:.2f}'

print(msg)