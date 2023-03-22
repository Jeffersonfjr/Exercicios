print('Digite seu sexo:\n1-Homem\n2-Mulher')
sexo=int(input('Opção: '))

print('Digite abaixo sua altura para realizarmos o calculo: ')
altura=float(input('Altura: '))

if sexo == 1:
    print('Seu peso ideal é: ',(72.7*altura)-58)
    
elif sexo == 2:
    print('Seu peso ideal é: ',(62.1*altura)-44.7)

else:
    print('Sexo incorreto')


