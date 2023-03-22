
morango = float(input('Qual é a quantidade de morango?\n'))
maca = float(input('Qual é a quantidade de maça?\n'))

if morango <= 5:
    morangoprice = morango * 2.5
else:
    morangoprice = morango * 2.2

if maca <= 5:
    macaprice = maca * 1.8
else:
    macaprice = maca * 1.5

if morango > 8 or morangoprice > 25:
    morangodesconto = morangoprice * 0.1
    print('O valor a ser pago de morangos é\nQuant: ', morango, ' KG\nTotal a ser pago: ', morangoprice-morangodesconto)
else:
    print('O valor a ser pago de morangos é\nQuant: ', morango, ' KG\nTotal a ser pago: ', morangoprice)

if maca > 8 or macaprice > 25:
    macadesconto = macaprice * 0.1
    print('O valor a ser pago de morangos é\nQuant: ', maca, ' KG\nTotal a ser pago: ', macaprice-macadesconto)
else:
    print('O valor a ser pago de morangos é\nQuant: ', maca, ' KG\nTotal a ser pago: ', macaprice)
