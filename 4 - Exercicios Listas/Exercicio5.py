# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.

lista = list(range(0,21))

par = []
impar = []

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'Pares: {par}\nImpares: {impar}')
