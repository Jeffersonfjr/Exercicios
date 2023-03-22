try:
    cm=(input('Insira o valor em cm(Caso o numero for decimal, utilize "." como separador): '))
    pi=3.14
    raio=float(cm)
    print('O raio do circulo: ', raio/(2*pi))
except:
    print('Digite um valor valido! ')
