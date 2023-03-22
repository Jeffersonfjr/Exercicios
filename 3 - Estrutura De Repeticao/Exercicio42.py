# Faça um programa que leia uma quantidade indeterminada de números positivos e conte 
# quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
# A entrada de dados deverá terminar quando for lido um número negativo.


def analise(lista):
    a = []
    b = []
    c = []
    d = []

    for i in lista:
        if i >= 0 and i <= 25:
            a.append(i)
        elif i >= 26 and i <= 50:
            b.append(i)
        elif i >= 51 and i <= 75:
            c.append(i)
        elif i >= 76 and i <= 100:
            d.append(i)

    return a, b, c, d


lista = []
contador = 0

while True:
    num = input('Digite um numero entre 0 e 100 para lista:\n')
    if not num.isnumeric:
        print('Digite um numero valido.')
        continue
    num = int(num)

    if num < 0 and num > 100:
        print('Digite um numero entre 0 e 100!')
        continue
    contador += 1
    lista.append(num)
    
    if contador == 10:
        break

novalista = analise(lista)

print(f'\n\nHouvera os seguintes resultados:\n'
      f'[  0- 25]: {len(novalista[0])}\n'
      f'[ 26- 50]: {len(novalista[1])}\n'
      f'[ 51- 75]: {len(novalista[2])}\n'
      f'[ 76-100]: {len(novalista[3])}\n')
