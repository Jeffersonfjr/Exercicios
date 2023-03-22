''' Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
    valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
    Os juros e a quantidade de parcelas seguem a tabela abaixo:"'''


def calculo(divida, parcela):
     
    if parcela > 1 and parcela < 4:
        juros = 0.10
    elif parcela > 3 and parcela < 7:
        juros = 0.15
    elif parcela > 6 and parcela < 10:
        juros = 0.20
    elif parcela > 9 and parcela < 13:
        juros = 0.25
    
    montante = divida + (divida * juros)

    # return f'VALOR DA DIVIDA : {divida} \nJUROS           : {juros*100} \nPARCELAS        : {parcela} \nVALOR DA PARCELA: {divida/parcela} '  
    return f'VALOR DA DIVIDA : {divida} \nJUROS           : {juros*100} \nPARCELAS        : {parcela} \nVALOR DA PARCELA: {divida/parcela} '  

while True:
    divida = input('Por favor, digite o valor total da divida: \n\t')
    if not divida.isdigit:
        print('Valor não é um numero, digite novamente.\n')
        continue
    divida = int(divida)
    
    parcela = input('Digite o numero de parcelas (TOTAL - 12X):\n\t')
    if not parcela.isdigit:
        print('Valor não é um numero, digite novamente.\n')
        continue
    parcela = int(parcela)

    
    print(calculo(divida, parcela))