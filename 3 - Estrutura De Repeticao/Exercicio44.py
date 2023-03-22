# Em uma eleição presidencial existem quatro candidatos. Os votos são informados 
# por meio de código. Os códigos utilizados são:

#   • Faça um programa que calcule e mostre:
#   • O total de votos para cada candidato;
#   • O total de votos nulos;
#   • O total de votos em branco;
#   • A percentagem de votos nulos sobre o total de votos;
#   • A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero."

a = 0
b = 0
c = 0
d = 0
e = 0
nulo = 0

print('Votação\n'
      '\t1 - Candidato A\n'
      '\t2 - Candidato B\n'
      '\t3 - Candidato C\n'
      '\t4 - Candidato D\n'
      '\t5 - Voto em BRANCO\n')

votacao = []
contador = 0
while True:
    voto = int(input('Digite o numero do seu candidato:\n'))
    votacao.append(voto)

    contador += 1

    if contador == 10:
        break

for i in votacao:
    if i == 1:
        a += 1
    elif i == 2:
        b += 1
    elif i == 3:
        c += 1
    elif i == 4:
        d += 1
    elif i == 5:
        e += 1
    else:
        nulo += 1

print(f'O resutado da votação foi o seguinte:\n\n'
      f'\tCandidato A: {100*(a/(len(votacao))):.2f}\n'
      f'\tCandidato B: {100*(b/(len(votacao))):.2f}\n'
      f'\tCandidato C: {100*(c/(len(votacao))):.2f}\n'
      f'\tCandidato D: {100*(d/(len(votacao))):.2f}\n'
      f'\tBRANCOS:     {100*(e/(len(votacao))):.2f}\n'
      f'\tNULOS:       {100*(nulo/(len(votacao))):.2f}\n')