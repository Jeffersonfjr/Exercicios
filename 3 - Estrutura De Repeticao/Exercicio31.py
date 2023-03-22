"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar.

O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total
da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco.

Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.
A saída deve ser conforme o exemplo abaixo:
 """
soma = 0
contador = 0

while True:
    contador += 1
    preco = float(input(f'Digite o preço do produto: '))

    if preco < 0:
        print('Valor invalido')
        continue

    if preco == 0:
        contador -= 1
        break

    soma += preco

troco = float(input('Qual o valor dado pelo cliente?\n'))
if troco < soma:
    while True:
        troco = float(input('Saldo insulficiente, digite um valor correto:\n'))

        if troco >= soma:
            break

if (troco - soma) >= 0:
    troco = troco - soma
else:
    troco = 0


print(f'O valor total dos {contador} itens da sua compra foi de:\n'
      f'R$ {soma}\n'
      f'O troco a devolver é de:\n'
      f'R$ {troco}')
