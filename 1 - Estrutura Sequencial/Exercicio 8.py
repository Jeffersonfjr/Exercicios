try:
    print('Digite o valor do seu Salario/h')
    sal=(input('Salario:'))
    salario=float(sal)

    print('Quantas horas trabalhadas no mes?')
    tempo=input('horas (em valor decimal): ')
    horas=float(tempo)

    print('Seu salario neste mês é: ',salario*horas)
except:
    print('Valor incorreto')
    