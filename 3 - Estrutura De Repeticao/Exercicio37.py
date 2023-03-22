"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu
código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo
código.
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo,
do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""


def gordo(x):
    nome = ''
    codigo = 0
    mgordo = 0
    for c, n, p, a in lista:
        if p > mgordo:
            codigo = c
            nome = n
            mgordo = p
    return f'O {codigo}:{nome} é o mais gordo com {mgordo} quilos'


def magro(x):
    nome = ''
    codigo = 0
    peso = 1000
    for c, n, p, a in lista:
        if p < peso:
            codigo = c
            nome = n
            peso = p
    return f'O {codigo}:{nome} é o mais magro com {peso} quilos'


def alto(x):
    nome = ''
    codigo = 0
    altura = 0
    for c, n, p, a in lista:
        if a > altura:
            codigo = c
            nome = n
            altura = a
    return f'O {codigo}:{nome} é o mais alto com {altura*100} cm'


def baixo(x):
    nome = ''
    codigo = 0
    altura = 1000
    for c, n, p, a in lista:
        if a < altura:
            codigo = c
            nome = n
            altura = a
    return f'O {codigo}:{nome} é o mais baixo com {altura*100} cm'


cont = 0
lista = []
while True:
    cont += 1
    nome = input('Digite sue nome: ')
    if nome == "0":
        break
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    banco = [cont , nome, peso, altura]
    lista.append(banco)
    print('')

print(gordo(lista))
print(magro(lista))
print(alto(lista))
print(baixo(lista))
