'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos
 • Álcool:
  • até 20 litros, desconto de 3% por litro
  • acima de 20 litros, desconto de 5% por litro
  • Gasolina:
  • até 20 litros, desconto de 4% por litro
  • acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de
    combustível (codificado da seguinte forma: A-álcool, G-gasolina),

    •calcule e imprima o valor a ser pago pelo cliente
     sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

comb = int(input('Qual é o combustivel desejado?\n1 - Gasolina\n2 - Alcool\n'))

while comb < 1 or comb > 2:
    print('Por favor escolha uma opção validade')
    comb = float(input('Qual é o combustivel desejado?\n1 - Gasolina\n2 - Alcool\n'))

else:
    if comb == 1:
        quant=float(input('Quantos litros:\n'))

        if quant <= 20.0:
            total=quant*(2.5-(2.5*0.04))
            print('O valor do combustivel será ', total)
        elif quant > 20:
            total = quant * (2.5 - (2.5 * 0.06))
            print('O valor do combustivel será ', total)

    else:
        quant = float(input('Quantos litros:\n'))

        if quant <= 20.0:
            total = quant * (1.9 - (1.9 * 0.03))
            print('O valor do combustivel será ', total)
        elif quant > 20:
            total = quant * (1.9 - (1.9 * 0.05))
            print('O valor do combustivel será ', total)
