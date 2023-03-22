n1=float(input('Digite a 1º nota:'))
n2=float(input('Digite a 1º nota:'))

media=(n1+n2)/2

while n1 > 10 or n2 > 10:

    print('Não pode haver notas maoires que "10"')

    n1=float(input('Digite a 1º nota:'))
    n2=float(input('Digite a 1º nota:'))

    media=(n1+n2)/2 

else:
    if media > 9.01 and media <= 10:
        print('A')
    
    elif media > 7.51 and media <= 9:
        print('B')

    elif media > 6.01 and media <= 7.5:
        print('C')

    elif media > 4.01 and media <= 6:
        print('D')
    
    elif media >= 0 and media <= 4:
        print('E')

    else:
        print('Não pode haver numero negativo')