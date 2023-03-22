"""
"Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
    Foram obtidos os seguintes dados:

  • Código da cidade;
  • Número de veículos de passeio (em 1999);
  • Número de acidentes de trânsito com vítimas (em 1999).

    Deseja-se saber:
       - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
       - Qual a média de veículos nas cinco cidades juntas;
       - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio."

"""

def states(lista):
    teste = 0
    contador = 0
    controle = 0
    for num, cid, car in lista:
        if num > controle:
            controle = num
            teste = contador
        contador +=1
    return lista[teste]


lista = []
ano = 1999

while True:
    try:
        cidade = int(input('Qual cidade ocorreu o acidente: '
                       '\nCIDADES DISPONIVEIS:\n'
                       '\t1 - São Caetano\n'
                       '\t2 - Santo André\n'
                       '\t3 - São Bernado\n\n'))
        if cidade == 1:
            cidade = 'São Caetano'
        elif cidade == 2:
            cidade = 'Santo André'
        elif cidade == 3:
            cidade = 'São Bernado'
        else:
            print(f'Valor "{cidade}" incorreto, por favor, digitar corretamente.\n\n"')
            continue
        veiculo = int(input('Qual o veiculo:\n'
                        'VEICULOS DISPONIVEIS\n'
                        '\t1 - Gol\n'
                        '\t2 - Ecosport\n'
                        '\t3 - Fiesta\n\n'))
        if veiculo == 1:
            veiculo = 'Gol'
        elif veiculo == 2:
            veiculo = 'Ecosport'
        elif veiculo == 3:
            veiculo = 'Fiesta'
        else:
            print(f'Valor "{veiculo}" incorreto, por favor, digitar corretamente.\n\n')
            continue
        num_acid = int(input('O numero de acidentes que aconteceu nesse ano:\n'))

        lista.append([num_acid,cidade,veiculo])

        ano += 1

        if ano == 2001:
            break
    except:
        print('Valor incorreto!')
        continue

estatistica = states(lista)

print(f'A cidade com mais acidentes é: {estatistica[1]}\n'
      f'O carro que mais esteve em acidetens foi o {estatistica[2]} com {estatistica[0]} acidentes')

