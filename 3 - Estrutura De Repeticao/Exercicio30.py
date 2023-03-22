"""
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de
preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
"""

lista = []

for i in range(1, 4):
    preco = float(input(f'Digite o preço do {i}º prudoto: '))

    if preco <= 0:
        print('valor invalido, será considerado o valor "0"')
        preco = 0

    lista.append(preco)

print('\nSua tabela de preço é a seguinte:\n')


for i, x in enumerate(lista, 1):
    print(f'Codigo: {i} - Preço: {x} ')

