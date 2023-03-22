"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.

"""
def media(lista):
    media = 0
    for i in lista:
        media += i
    return media/len(lista)


soma = 0
lista = []

while True:
    temperatura = input(f'Digite o preço do produto:(DIGITE "SAIR" PARA ENCERRAR)\n')

    if temperatura.lower() == 'sair':
        break

    if not temperatura.isdigit():
        print('Digite um numero valido\n')
        continue
    temperatura = float(temperatura)


    lista.append(temperatura)


print(f'\nINFORMAÇÕES:\n'
      f'MÉDIA DE TEMPERATURAS: {media(lista)}\n'
      f'MAIOR DE TEMPERATURAS: {max(lista)}\n'
      f'MENOR DE TEMPERATURAS: {min(lista)}')

