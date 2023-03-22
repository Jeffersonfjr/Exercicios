sal=float(input('Digite o Salario do funcionario:\n'))

inss=sal*0.1
fgts=sal*0.11
sind=sal*0.03

if sal <= 900:
    ir=0

elif sal > 900 and sal <= 1500:
    ir=sal*0.05

elif sal > 1500 and sal <= 2500:
    ir=sal*0.1

elif sal > 2500:
     ir=sal*0.20

print('Salario bruto: ',sal,'\nINSS :',inss,'\nSindicato: ',sind,'\nFGTS: ',fgts,'\nIRRF: ',ir,'\nSalario Liquido: ',sal-(inss+fgts+sind+ir))