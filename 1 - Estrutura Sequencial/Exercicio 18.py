mb=int(input('Digite o tamanho do arquivo(em megabytes): '))
velocidade=int(input('Digite a velocidade da internet(em megabytes): '))

import math

tempo=math.ceil(mb/velocidade)

print('O tempo de download sera: ', tempo)