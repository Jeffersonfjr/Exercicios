print('Digite o tamanho da area a ser pintada em metros²')

area=float(input("Area: "))

import math

lata=math.ceil((area/3)/18)

if lata <= 1:
    print('A quantidade de latas de 18 litros será de: 1 lata')

else:
    print('A quantidade de latas de 18 litros será de: ',lata,' latas')