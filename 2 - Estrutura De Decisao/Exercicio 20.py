nota1=float(input('Digite a 1º nota: '))
nota2=float(input('Digite a 2º nota: '))
nota3=float(input('Digite a 3º nota: '))

media=float((nota1+nota2+nota3)/3)

while nota1<0 or nota2<0 or nota3<0 or nota1>10 or nota2>10 or nota3>10:
    print('Não pode haver notas maiores que 10 ou menores que 0')
    nota1=float(input('Digite a 1º nota: '))
    nota2=float(input('Digite a 2º nota: '))
    nota3=float(input('Digite a 3º nota: '))

    media=float((nota1+nota2+nota3)/3)
    
else:
    
    if media>=7 and media<=9:
        print('Aprovado')

    elif media<7 and media>=0:
        print('Reprovado')

    elif media==10:
        print('Aprovado com Distinção')