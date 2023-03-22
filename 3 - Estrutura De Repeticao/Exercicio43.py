# "O cardápio de uma lanchonete é o seguinte:
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do 
# pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado."

cardapio = {
    100 : ['Cachorro-quenta', 1.20],
    101 : ['Bauro simples  ', 1.30],
    102 : ['Bauro com ovo  ', 1.50],
    103 : ['Hambuguer      ', 1.20],
    104 : ['X-burguer      ', 1.30],
    105 : ['Refrigerante   ', 1.00],
}
pedido = []

print('Escolha seus lanches: \n')

for i , x in cardapio.items():
    print(f'COD: {i} - Produto: {x[0]} - Preço: {x[1]:.2f} ')

while True:
    produto = int(input('\nQual é o lanche desejado:\n'))
    if produto < 100 or produto > 105:
        print('\nDigite um valor do cardapio.')
        for i , x in cardapio.items():
            print(f'COD: {i} - Produto: {x[0]} - Preço: {x[1]:.2f} ')
        continue

    quantidade = int(input('Quantos:\n'))

    pedido.append([cardapio[produto][0],(cardapio[produto][1]*quantidade), quantidade])

    sair = input('\nDeseja sair?\n\t1 - Sim\n\t2 - Não\n')

    if sair == '1':
        break

print('\nA DESCRIÇÃO DO SEU PEDIDO:\n')

total = 0

for x, y, z in pedido:
    print(f'PRODUTO: {x} - QUANTIDADE: {z} - VALOR: R$ {y:.2f} ')
    total += y

print(f'\tTotal: {total:.2f}  ')