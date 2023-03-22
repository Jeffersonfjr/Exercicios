"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""
base = int(input('Digite a base do numero:\n'))
expo = int(input('Digite o expoente:\n'))

soma = base
pote = base

for i in range(1, expo):
    pote = base * pote

print(pote)
