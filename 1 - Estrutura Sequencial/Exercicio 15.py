print('Digite o valor do seu Salario/h')
sal=float(input('Salario:'))

print('Quantas horas trabalhadas no mes?')
tempo=float(input('horas (em valor decimal): \n'))
   
bruto=sal*tempo
ir=bruto*(11/100)
inss=bruto*(8/100)
sindicato=bruto*(5/100)
liquido=bruto-ir-inss-sindicato

print('+ Salário Bruto : R$',bruto,'\n- IR (11%) : R$',ir,'\n- INSS (8%) : R$',inss,'\n- Sindicato ( 5%) : R$',sindicato,'\n= Salário Liquido : R$',liquido)

