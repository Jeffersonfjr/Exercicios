"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido
por eles.
"""


def criar_lista(a, b):
    for i in range(a+1,b):
        print(i)


a = int(input("Digite o primeiro numero:\n"))
b = int(input("Digite o ultimo numero:\n"))

criar_lista(a,b)
