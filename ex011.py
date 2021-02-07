#DESAFIO 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m².

largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

area = largura * altura
litros = area/2

msg1 = 'Sua parede tem a dimensão {}x{} e sua área é de {} m².'.format(largura, altura, area)
msg2 = 'Para pintar essa parede, você precisará de {} l de tinta.'.format(litros)

print(msg1)
print(msg2)