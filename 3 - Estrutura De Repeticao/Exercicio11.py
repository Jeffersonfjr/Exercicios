
def criar_lista(a, b):
    soma = 0
    for i in range(a+1,b):
        print(i)
        soma += i
    print(f'\nA soma desses valores é {soma}')


a = int(input("Digite o primeiro numero:\n"))
b = int(input("Digite o ultimo numero:\n"))

criar_lista(a,b)