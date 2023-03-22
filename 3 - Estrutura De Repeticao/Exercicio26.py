"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

quantidade = int(input('Digite o numero de pessoas que terão que votar:\n'))
contador = 0
candidato1 = 0
candidato2 = 0

print('Você pode votar em:\n'
      'Candidato1 - 1\n'
      'Candadito2 - 2\n ')

while True:
    contador += 1
    voto = int(input('Digite o seu voto:\n'))

    if voto == 1:
        candidato1 += 1

    elif voto == 2:
        candidato2 += 1

    else:
        print('Voto anulado')

    if contador == quantidade:
        break

print(f'O Resutado da eleição foi o seguinte:\n'
      f'Candidato1 = {candidato1}\n'
      f'Candidato2 = {candidato2}\n')