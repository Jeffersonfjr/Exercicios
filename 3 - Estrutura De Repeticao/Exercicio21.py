"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""


def primo(x):
    for i in range(2, x):
        if x == i:
            continue
        if (x % i) == 0:
            return 1

    return 0


numero = int(input("Digite um numero: "))


if primo(numero) == 1:
    print('O Numero não é primo')
if primo(numero) == 0:
    print('O Numero é primo')

