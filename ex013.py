#DESAFIO 013: Faça um algotitmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do Funcionário? R$ '))

salario_com_aumento = salario + (salario * 0.15)

print(f'Um funcionário que ganhava R$ {salario:.2f}, com 15% de aumento, passa a receber R$ {salario_com_aumento:.2f}')
