"""
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que
o cliente comprou e ao lado o valor da conta.
Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços.
Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50
produtos, conforme o exemplo abaixo:

"""

lista = []

for i in range(1,4):
    preco = float(input(f'Digite o preço do {i}º prudoto: '))

    if preco <= 0:
        print('valor invalido, será considerado o valor "0"')
        preco = 0

    lista.append(preco)

print('\nSua tabela de preço é a seguinte:\n')


for i, x in enumerate(lista, 1):
    print(f'Codigo: {i} - Preço: {x} ')
