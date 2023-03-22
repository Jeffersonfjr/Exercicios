"""
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário.
"""
cont = 0
def numprimo(x):
    lista = [2,3]
    global cont

    for i in range(2 , x):
        for n in range(2 , i):
            if i % 2 == 0:
                cont += 1
                break
            elif i % 3 == 0:
                cont += 1
                break
            else:
                if i in lista:
                    pass
                else:
                    lista.append(i)


    return lista


num = int(input('Digite um valor:\n'))

for i in numprimo(num):
    print(i)

print(f'\n O numero de divisoes para chegar a esse valor foi de {cont}')