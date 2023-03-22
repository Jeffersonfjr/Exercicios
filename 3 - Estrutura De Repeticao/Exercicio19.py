
a = []
soma = 0

while True:

    if len(a) <= 4:
        x = int(input('Digite um numero: '))
        if x < 0 or x > 1000:
            print('Apenas aceitamos numeros entra 0 e 1000.\n tente novamente!')
            continue


        a.append(x)
        soma += x
    else:
        break


print(f'O maior numero digitado foi {max(a)}')
print(f'O maior numero digitado foi {min(a)}')
print(f'A soma dos numeros digitados é {soma}')

