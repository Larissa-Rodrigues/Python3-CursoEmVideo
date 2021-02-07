#DESAFIO 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço do produto? R$ '))

preco_com_desconto = preco - (preco * 0.05)

msg = 'O preço que custava R$ {:.2f}, na promoção de 5% vai custar R$ {:.2f}'.format(preco, preco_com_desconto)

print(msg)

