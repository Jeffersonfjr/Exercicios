lado1=input('Digite o 1º lado: ')
lado2=input('Digite o 2º lado: ')
lado3=input('Digite o 3º lado: ')

if lado1 == lado2 == lado3:
    print('Seu triangulo é equilaterado')
    
elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado3 == lado2 != lado1 or lado3 == lado1 != lado2:
    print('Seu triangulo é isoseles')
    
elif lado1 != lado2 != lado3:
    print('Seu triangulo é escaleno')  