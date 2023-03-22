"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

a = []
soma = 0

while True:
    if len(a) <= 9:
        x = int(input('Digite um numero: '))
        a.append(x)
        soma += x
    else:
        break


print(f'O maior numero digitado foi {max(a)}')
print(f'O maior numero digitado foi {min(a)}')
print(f'A soma dos numeros digitados é {soma}')

