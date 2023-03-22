"""
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número
inteiro e determine se ele é ou não um número primo.
"""

def numprimo(x):
    primo = True
    for i in range(2, x):
        if x % i == 0:
            primo = False
            break

    return primo



num = int(input('Digite um valor:\n'))

print('O numero é primo' if numprimo(num) == True else 'O Numero não é primo')