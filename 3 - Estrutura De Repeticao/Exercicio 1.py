"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.
"""
sair = False
while not sair == True:
    num1 = input('Digite um valor de 0 a 10:\n')

    while not num1.isdigit():
        print(f'Você digitou {num1} que não é um numero')
        num1 = input('Digite um valor de 0 a 10:\n')

    else:
        num1 = int(num1)
        if num1 < 0 or num1 > 11:
            print(f'Você digitou {num1}, que não está entre 0 e 10')
        else:
            print(f'Você digitou {num1}, correto!')
            fim = input('Deseja encerrar:\nS - Sim\nN - Não\n')
            fim = fim.upper()

            if fim == "S":
                sair = True

else:
    print('Encerrado')
