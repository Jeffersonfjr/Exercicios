valor=float(input('Digite um valor: \n'))

opcao=int(input('O que você quer saber?\n1 - Se o numero é "par ou impar"\n2 - Se o numero é "Positivo ou Negativo"\n3 - Se o numero é "Inteiro ou Decimal"\n'))

while opcao<=0 or opcao>=4:
    print('\nPor favor, escolha uma opção valida\n\n')
    opcao=int(input('O que você quer saber?\n1 - Se o numero é "par ou impar"\n2 - Se o numero é "Positivo ou Negativo"\n3 - Se o numero é "Inteiro ou Decimal"\n'))

else:
    
    if opcao==1:
        if valor%2==0:
            print('par')
        else:
            print('impar') 
        
    elif opcao==2:
        if valor>=1:
            print('o valor é positivo')
        elif valor<=-1:
            print('O valor é negativo')
        else:
            print('O valor é 0')
    
    elif opcao==3:
        if valor%1==0:
            print('inteiro')
        else:
            print('decimal')

