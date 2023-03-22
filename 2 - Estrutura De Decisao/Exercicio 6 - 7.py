n1=int(input('Insira o 1º numero: '))
n2=int(input('Insira o 2º numero: '))
n3=int(input('Insira o 3º numero: '))

while n1 == n2 or n1 == n3 or n2 == n3:
    print('Não pode haver numeros iguais, digite novamente')
    n1=int(input('Insira o 1º numero: '))
    n2=int(input('Insira o 2º numero: '))
    n3=int(input('Insira o 3º numero: '))

else:

    maior=n1
    menor=n1

    if n2 > maior:
        maior=n2
        
    if n3 > maior:
        maior=n3

    if n2 < menor:
        menor=n2
        
    if n3 < menor:
        menor=n3
    
    print('O maior numero é: ', maior,' e o menor é: ',menor)
