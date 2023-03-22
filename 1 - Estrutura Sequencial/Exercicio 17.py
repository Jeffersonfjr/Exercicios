print('Digite o tamanho da area a ser pintada em metros²')

area=float(input("Area: "))

import math

lata=math.ceil((area/6)/18)



if lata <= 1:

    latinha=math.ceil((area/6)/3.6)
    preco=float(latinha*25.00)

    print('Serão necessarias: ',latinha, ' de tinta de 3,6 litros e a compra ficar ano valor de : ',preco)

elif lata > 1:
    
    latinha=math.ceil((area/6)/3.6)
    preco1=float(lata*80.00)
    preco2=float(latinha*25.00)

    print('São necessarios:\n',lata,' lata(s) de 18L no valor de: ',preco1,'\nou\n',latinha,' lata(s) de 3,6L, no preço de : ',preco2)

else:
    print('A quantidade de latas de 18 litros será de: ',lata,' latas')