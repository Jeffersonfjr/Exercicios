# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
# Imprima as consoantes.


lista = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' ,'j']
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = []


for i in lista:
    if i in vogais:
        continue

    consoantes.append(i)

print(f'Consoantes: {consoantes}\nQuantidade {len(consoantes)}')