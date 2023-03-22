# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
# Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas 
# pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada 
# (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
# As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

salto = []
media = 0
contador = 0
nome = input('Digite seu nome:\n')

if nome == "":
    print('Não foi digitado valor')
else:
    while True:
        altura = input('Digite a nota do juiz: ')
        if not altura.isnumeric:
            print('\nDigite um valor valido.\n')
            continue
        altura = float(altura)

        salto.append(altura)

        contador += 1
        if contador == 7:
            break


print(f'\n\nAtleta: {nome} \n\n')

for i in salto:
    print(f'Nota: {i} m')


print(f'\n\nResultado final:\n'
      f'Atleta: {nome}\n'
      f'Melhor nota: {max(salto)}\n'
      f'Pior nota: {min(salto)}\n')

salto.pop(salto.index(max(salto)))
salto.pop(salto.index(min(salto)))

for i in salto:
    media += i

media = media/len(salto)
print(f'Media; {media}')

