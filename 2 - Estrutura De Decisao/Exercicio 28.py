"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá
ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo
de pagamento, valor do desconto e valor a pagar.
"""

carne = input("Qual a carne adquirida?\nF - Filé Duplo\nA - Alcatra\nP - Picanha\n")
carne = carne.upper()
resposta1 = False
resposta2 = False

if carne == "F":
    resposta1 = True
elif carne == "A":
    resposta1 = True
if carne == "P":
    resposta1 = True

while not resposta1 == True:
    print(f'Você digitou {carne}, que não é um parametro correto, por favor, digite novamente.')
    carne = input("Qual a carne adquirida?\nF - Filé Duplo\nA - Alcatra\nP - Picanha\n")
    carne = carne.upper()

    if carne == "F":
        resposta1 = True
    elif carne == "A":
        resposta1 = True
    if carne == "P":
        resposta1 = True
else:
    pergunta = input("Houve outro tipo de carne?\nS - Sim\nN - Não\n")
    pergunta = pergunta.upper()

    if pergunta == "S":
        resposta2 = True
    elif pergunta == "N":
        resposta2 = True

    while not resposta2 == True:
        print(f'Você digitou {pergunta}, que não é um parametro correto, por favor, digite novamente.')
        pergunta = input("Houve outro tipo de carne?\nS - Sim\nN - Não\n")
        pergunta = pergunta.upper()

        if pergunta == "S":
            resposta2 = True
        elif pergunta == "N":
            resposta2 = True

    else:

        if pergunta == "S":
            print('Não é possivel adquirir mais de um tipo de carne.')

        else:
            quilo = int(input('Quantos quilos de carne você esta adquirindo?\n'))
            cartao = input('Você usara cartão?\nS - Sim\nN - Não\n')
            cartao = cartao.upper()
            preco = 0
            if carne == "F":
                if quilo <= 5:
                    preco = 4.90
                else:
                    preco = 5.80
            elif carne == "A":
                if quilo <= 5:
                    preco = 5.90
                else:
                    preco = 6.80
            elif carne == "P":
                if quilo <= 5:
                    preco = 6.90
                else:
                    preco = 7.80

            if cartao == "S":
                preco = preco - (preco * 0.05)

            preco = preco * quilo
            print(f'Você pagara o valor de {preco:.2f} em carnes')
