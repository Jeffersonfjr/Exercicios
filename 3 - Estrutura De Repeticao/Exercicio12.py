"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo
"""

x = int(input('Digite o numero que você deseja ver a tabuada:\n'))

for i in range(1,11):
    print(f'{x} X {i} = {x*i}')
