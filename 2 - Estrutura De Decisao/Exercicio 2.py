try:
    valor1=int(input('Digite um valor '))

    if valor1 >= 1:
        print('O numero é positivo')

    elif valor1 == 0:
        print('O valor é 0 (Não é positivo, nem negativo')

    elif valor1 <= -1:
        print('O valor é negativo')

    else:
        print('valor incorreto')
        
except:
    print('valor incorreto')
