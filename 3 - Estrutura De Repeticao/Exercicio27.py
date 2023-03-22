"""
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
"""

quantidade = int(input('Digite o numero de turmas:\n'))
contador = 0
soma = 0

while True:
    contador += 1
    alunos = int(input(f'Digite o numero de alunos da turma {contador}: '))
    if alunos > 40:
        contador -= 1
        print('Valor de turma invalido, não pode haver mais de 40 alunos.')
        continue

    soma += alunos

    if contador == quantidade:
        break

soma = round(soma/quantidade)
print(f'O numero médio das {quantidade} turmas, é de {soma}')