numero=(int(input('Digite um numero: ')))

unidade=int(numero%10)

numero=(numero-unidade)/10

dezena=int(numero%10)

numero=(numero-dezena)/10

centena=int(numero%10)

print('Nesse numero há: ',centena,' centena(s), ',dezena,' dezena(s) e ',unidade,'unidade(s)')
