#DESAFIO 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# strip elimina os espaços
cidade = input('Em qual cidade você nasceu? ').strip()

print(cidade[0:5].upper() == 'SANTO')