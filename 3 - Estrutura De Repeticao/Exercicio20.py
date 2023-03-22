"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial
a números inteiros positivos e menores que 16.
"""
while True:
    num = int(input('Digite um numero: '))
    if num > 16 or num < 0:
        print('Nâo é possivel utilizar numeros maiores que 16 e menos de 0')
        continue

    fat = 1
    for i in range(num, 0, -1):
        fat = i * fat

    print(fat)
