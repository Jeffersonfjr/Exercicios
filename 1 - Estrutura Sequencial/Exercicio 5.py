try:
    metro=(input('Insira o valor em metros a ser convertido(Caso o numero for decimal, utilize "." como separador): '))
    cm=float(metro)
    print('O valor digitado em centimetro é: ', metro*100)
except:
    print('Digite um valor valido! ')
