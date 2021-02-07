#DESAFIO 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

valor = float(input('Digite um valor: '))

inteiro = valor // 1

msg = f'O valor digitado foi {valor} e a sua porção inteira é {inteiro:.0f}'

print(msg)