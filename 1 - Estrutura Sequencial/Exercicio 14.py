print('Olá, Por favor, digite abaixo quantos quilos foram pescados:')

peso=float(input('Quantidade: '))

if peso > 50:
    excesso=peso-50
    multa=excesso*4
    print('O Valor excendente foi:\n',excesso,'quilos\n\nO valor de multa foi:\nR$ ',multa)

else:
    print('Não houve excedente.')