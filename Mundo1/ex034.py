#DESAFIO 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Considere: Para salários superiores a R$ 1250,00 calcule um aumento de 10%. Para salários inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o salário do funcionário? R$ '))

if salario <= 1250.00:
    salario_atualizado = salario + (salario * 0.15)
else:
    salario_atualizado = salario + (salario * 0.1)

print(f'Quem ganhava {salario:.2f} passa a ganhar R$ {salario_atualizado:.2f} agora.')