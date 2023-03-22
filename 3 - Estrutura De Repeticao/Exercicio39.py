"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno
mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

lista = []
while True:
    nome = input('Digite o nome do aluno: ')
    if nome == "0":
        break
    altura = float(input('Digite sua altura: '))
    lista.append([altura, nome])
    print('')

lista.sort(reverse=True)

for i in lista:
    print(i)