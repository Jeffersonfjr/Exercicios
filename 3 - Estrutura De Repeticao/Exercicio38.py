"""
"Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

  • Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
  • Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
  • A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.

  Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo
  que o usuário digite o salário inicial do funcionário."

"""

ano = 1995
salario = 1000.00
aumento = 1.5
lista = []

while True:
    lista.append([{ano:salario},aumento])
    salario = salario + (salario * (aumento/100))

    if ano < 1996:
        ano += 1
        continue
    if ano >= 2000:
        break
    aumento = aumento * 2
    ano += 1

for i in lista:
    print(i)