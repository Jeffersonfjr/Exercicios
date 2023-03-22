# Faça um Programa que peça as quatro notas de 10 alunos, 
# calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0

aluno = []
media = []
contador = 0

while True:
    media_nota = 0
    nome = input('\nDigite o nome do aluno: ')
    aluno.append(nome)
    while contador < 4:
        nota = float(input(f'Digite a {contador + 1}º nota:'))
        media_nota += nota
        contador += 1

    media.append(media_nota/contador)
    
    contador = 0

    sair = input('\nHa mais algum aluno?\n\t1 - Sim\n\t2 - Não\n')

    if sair == "2":
        break

for m in  media:
    if m >= 7:
        print(f'Aluno: {aluno[contador]}\nMedia: {m}\n')
        contador += 1
