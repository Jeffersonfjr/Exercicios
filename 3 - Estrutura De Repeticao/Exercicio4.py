"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.
"""

a = 80000
b = 200000

crescimento_a = 0.03
crescimento_b = 0.015

ano = 0


while a < b:

    a = a * 1.03
    b = b * 1.015

    ano += 1

else:
    print(f'A cidade A, ultrapassou a cidade B em {a - b}, após {ano}')
    