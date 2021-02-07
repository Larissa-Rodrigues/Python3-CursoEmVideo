#DESAFIO 014: Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

celsius = float(input('Informoe a temperatura em °C: '))
fahrenheit = ((celsius * 9)/5) + 32

msg = f'A temperatura de {celsius:.2f} °C corresponde a {fahrenheit:.2f} °F!'

print(msg)