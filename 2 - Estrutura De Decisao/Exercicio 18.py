dia=int(input('Digite o dia: '))
mes=int(input('Digite o mês: '))
ano=int(input('Digite o ano: '))

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    if dia>=1 and dia<=31:
        print('A data: ',dia,'/',mes,'/',ano,' é valida.')
    
    else:
         print('A data: ',dia,'/',mes,'/',ano,' não é valida.')
         
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if dia>=1 and dia<=30:
        print('A data: ',dia,'/',mes,'/',ano,' é valida.')
    
    else:
         print('A data: ',dia,'/',mes,'/',ano,' não é valida.')
         
elif (mes == 2):
    if dia == 29 and (ano%4 == 0 and ano%100!= 0) or ano%400 == 0:
        print('A data: ',dia,'/',mes,'/',ano,'é valida.')
    elif dia >=1 and dia<=28:
        print('A data: ',dia,'/',mes,'/',ano,'é valida.')
    else:
        print('A data: ',dia,'/',mes,'/',ano,' não é valida.')