"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

"""

num = int(input('Digite um numero: '))
fat = 1

for i in range(num, 0, -1):
    fat = i * fat

print(fat)
