n1=int(input('Insira o 1º numero: '))
n2=int(input('Insira o 2º numero: '))
n3=int(input('Insira o 3º numero: '))

while n1 == n2 or n1 == n3 or n2 == n3:
    print('Não pode haver numeros iguais, digite novamente')
    n1=int(input('Insira o 1º numero: '))
    n2=int(input('Insira o 2º numero: '))
    n3=int(input('Insira o 3º numero: '))

else:

    if n1 > n2 > n3:
        print(n1,' - ',n2,' - ',n3)

    elif n1 > n3 > n2:
        print(n1,' - ',n3,' - ',n2)
    
    elif n2 > n1 > n3:
        print(n2,' - ',n1,' - ',n3)

    elif n2 > n3 > n1:
        print(n2,' - ',n3,' - ',n1)

    elif n3 > n1 > n2:
        print(n3,' - ',n1,' - ',n2)

    elif n3 > n2 > n1:
        print(n3,' - ',n2,' - ',n1)

