valor=int(input('Qual o valor desejado de saque? (Valor minimo é de R$ 10.00 e o maximo de R$ 600.00) \n'))
tela=valor
while valor<=10 or valor>=600:
    valor=int(input('valor invalido\nPor favor, digite o valor desejado de saque? (Valor minimo é de R$ 10.00 e o maximo de R$ 600.00 \n'))
    tela=valor
else:
    cem=int(valor/100)
    
    valor=valor-(cem*100)
    
    cinquenta=int(valor/50)
    
    valor=valor-(cinquenta*50)
    
    dez=int(valor/10)
    
    valor=valor-(dez*10)
    
    cinco=int(valor/5)
    
    valor=valor-(cinco*5)
    
    um=int(valor/1)
    
    print('Voce ira sacar o total de : ',tela,' com as seguintes notas:\n',cem,' nota(s) de cem real(ais)\n',cinquenta,' nota(s) de cinquenta real(ais)\n',dez,' nota(s) de dez real(ais)\n',cinco,' nota(s) de cinco real(ais)\n',um,' nota(s) de um real(ais)')    