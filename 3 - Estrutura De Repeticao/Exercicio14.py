"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a
quantidade de números impares.
"""


def contador(lista):
    par = 0
    impar = 0

    for i in lista:
        if i % 2 == 0:
            par += 1
        else:
            impar += 1

    print(f'\tPar: {par}\n\tImpar: {impar}')


num = []

for i in range(1,11):
    a = int(input('Digite um numero: '))
    num.append(a)

contador(num)