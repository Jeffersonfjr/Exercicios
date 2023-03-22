"""
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados
também pelo usuário, conforme exemplo abaixo:

"""

inicio = int(input('Digite o valor inicial: '))
fim = int(input('Digite o numero final: '))

while True:
    if fim < inicio:
        print('O valor inicial não pode ser maior que o inicial')
    else:
        break

multi = int(input('Qual valor de taboada você deseja: '))

print(f'\nSerá mostrada a taboado do {multi}, se iniciando no {inicio} e encerrando no {fim}.\n')

for i in range(inicio, fim + 1):
    print(f'{multi} X {i} = {multi*i}')