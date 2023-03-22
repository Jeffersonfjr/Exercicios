gabarito = {
    1:"A",
    2:"B",
    3:"C",
    4:"D",
    5:"E",
    6:"E",
    7:"D",
    8:"C",
    9:"B",
    10:"A",
}

contador = 1
aluno_num = 1
nota = 0

aluno = []

while True:
    nome = input('Digite seu nome: \n')

    
    while True:
        print(f'\nQuestão {contador}')
        resposta = input('Digite sua resposta:\n')

        if gabarito[contador] == resposta.upper():
            nota += 1

        contador +=1
        if contador == 11: 
            break

    aluno.append([aluno_num, nome , nota])
    
    sair = input('Ha mais alunos?\n\t1-Sim\n\t2-Não\n')
    
    if sair == "2":
        break
    
    aluno_num += 1
    contador = 1

media = 0

for num, nome_aluno, nota_aluno in aluno:
    print(f'Numero do aluno: {num} - NOME: {nome_aluno} - NOTA: {nota_aluno}')
    media += nota
   

print(f'\nA maior nota da sala foi de ... do aluno: ...\n'
      f'A media de notas da sala foi de: {media/len(aluno):.0f}\n'
      f'O numero de alunos que realizarão a prova foi de {len(aluno)}.')