"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""

quantidade = int(input('Digite o numero de notas que serão calculadas:\n'))
contador = 0
soma = 0

while True:
    contador += 1
    nota = int(input('Digite a nota: '))
    soma += nota

    if contador == quantidade:
        break

print(f'A media das suas notas é de {round(soma/quantidade)}')


