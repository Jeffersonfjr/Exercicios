"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto
em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""

quantidade = int(input("Digite o numero de CD's na coloção:\n"))
contador = 0
soma = 0

while True:
    contador += 1
    cd = float(input(f'Qual o valor pago no cd {contador}: '))

    soma += cd

    if contador == quantidade:
        break

print(f'Há {quantidade} CDs na coleção, foi investido um total de {soma}, '
      f'e o valor medio para cada um é de {soma/quantidade}')