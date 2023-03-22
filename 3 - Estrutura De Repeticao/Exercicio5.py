"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""

a = input('Digite a população da cidade A:\n')
b = input('Digite a população da cidade b:\n')

crescimento_a = input('Digite a taca de crescimento da cidade A:\n')
crescimento_b = input('Digite a taca de crescimento da cidade b:\n')

if not a.isdigit() or not b.isdigit() or not crescimento_a.isdigit() or not crescimento_b.isdigit():
    print('Favor, digite valores validos')

a = int(a)
b = int(b)
crescimento_a = 1 + (float(crescimento_a)/100)
crescimento_b = 1 + (float(crescimento_b)/100)

ano = 0

if a < b:

    while True:

        if a > b:
            print(f'A cidade A, ultrapassou a cidade B em {a - b}, após {ano} anos')
            break
        a += round(a * crescimento_a)
        b += round(b * crescimento_b)
        ano += 1
elif b < a:
    while True:

        if b > a:
            print(f'A cidade B, ultrapassou a cidade A em {b - a}, após {ano} anos')
            break
        a += round(a * crescimento_a)
        b += round(b * crescimento_b)
        ano += 1
else:
    print('Os valores das daus cidades são iguais.')
