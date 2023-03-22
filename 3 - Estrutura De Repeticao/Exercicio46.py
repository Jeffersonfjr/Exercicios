# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
# No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
# O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa 
# que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe 
# a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e 
# depois calcular a média). Faça uso de uma lista para armazenar os saltos. 
# Os saltos são informados na ordem da execução, portanto não são ordenados. 
# O programa deve ser encerrado quando não for informado o nome do atleta. 

salto = []
media = 0
contador = 0
nome = input('Digite seu nome:\n')

if nome == "":
    print('Não foi digitado valor')
else:
    while True:
        altura = input('Digite a altura do Saldo:\n')
        if not altura.isnumeric:
            print('\nDigite um valor valido.\n')
            continue
        altura = float(altura)

        salto.append(altura)
        contador += 1

        if contador == 5:
            break


print(f'\n\nAtleta: {nome} \n\n'

f'Primeiro Salto: {salto[0]} m\n'
f'Segundo Salto: {salto[1]} m\n'
f'Terceiro Salto: {salto[2]} m\n'
f'Quarto Salto: {salto[3]} m\n'
f'Quinto Salto: {salto[4]} m\n'
f'\n'
f'Melhor salto:  {max(salto)} m\n'
f'Pior salto: {min(salto)} m')

salto.pop(salto.index(max(salto)))
salto.pop(salto.index(min(salto)))

for i in salto:
    media += i

media = media/len(salto)

print(f'Média dos demais saltos: {media} m\n\n'
      f'Resultado final:'
      f'{nome}: {media}')



