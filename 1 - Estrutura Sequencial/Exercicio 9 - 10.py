
print('Você deseja fazer qual conversão?\n1 - Celsius -> Fahrenheit\n2 - Fahrenheit -> Celsius')

opcao=int(input("Opção: "))

while (opcao != 1) or (opcao != 2):
    if opcao == 1:
        print('Para realizarmos a conversão de "Celsius" para " Fahrenheit')
        celcius1=input('Digite o valor dos graus Celcius: ')
        fahr1=float(celcius1)
    
        print('Este valor em Fahrenheit é: ',(fahr1*1.8)+32,'º')

    elif opcao == 2:
        print('Para realizarmos a conversão de "Fahrenheit" para "Celsius')
        fahr2=input('Digite o valor dos graus Fahrenheit: ')
        
        celcius2=float(fahr2)
                
        print('Este valor em Celsius é: ',(5*((celcius2-32)/9)),'º')
    
    else:
        print('Digite um valor correto.')
else:
        print('Por favor digite uma opção valida. (1 ou 2)')
        