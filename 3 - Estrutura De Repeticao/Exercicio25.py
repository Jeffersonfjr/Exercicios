"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
conforme a média calculada.
"""

quantidade = int(input('Digite o numero de pessoas que terão a idade calculadas:\n'))
contador = 0
soma = 0

while True:
    contador += 1
    nota = int(input('Digite a idade da pessoa: '))
    soma += nota

    if contador == quantidade:
        break

soma = round(soma/quantidade)

if soma > 0 and soma <= 25:
    print(f'A média de idade é de {soma}, há mais jovens na turma')
elif soma >= 26 and soma <= 60:
    print(f'A média de idade é de {soma}, há mais adultos na turma')
elif soma >= 61:
    print(f'A média de idade é de {soma}, há mais idosos na turma')