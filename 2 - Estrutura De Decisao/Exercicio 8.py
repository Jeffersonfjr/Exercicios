n1=float(input('Digite o valor do 1º produto: '))
n2=float(input('Digite o valor do 2º produto: '))
n3=float(input('Digite o valor do 3º produto: '))

while n1 == n2 or n1 == n3 or n2 == n3:
    print('Não pode haver numeros iguais, digite novamente')
    n1=float(input('Digite o valor do 1º produto: '))
    n2=float(input('Digite o valor do 2º produto: '))
    n3=float(input('Digite o valor do 3º produto: '))

else:

    menor=n1

    if n2 < menor:
        menor=n2
        
    if n3 < menor:
        menor=n3
    
    print('O produto mais barato é', menor)