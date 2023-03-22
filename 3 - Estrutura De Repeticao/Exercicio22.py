def primo(x):
    lista = []
    pri = False
    for i in range(2, x):
        if x % i == 0:
            pri = True
            lista.append(i)
            
    if pri:
        return f'O numero não é primo, e é divisivel pelos numeros:\n{lista}'
    else:
        return 'O numero é primo'


num = int(input('Digite um numero:\n'))

print(primo(num))
