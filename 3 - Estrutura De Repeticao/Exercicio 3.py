'''
 • Nome: maior que 3 caracteres;
  • Idade: entre 0 e 150;
  • Salário: maior que zero;
  • Sexo: 'f' ou 'm';
  • Estado Civil: 's', 'c', 'v', 'd';
'''
while True:
    nome = input('\nDigite seu nome: ')
    idade = input('\nDigite sua idade: ')
    salario = input('\nDigite seu salario: ')
    sexo = input('\nDigite seu sexo: (f)eminino ou (m)asculino ')
    civil = input(' \nDigite seu etado civil: (s)olteiro - (c)casado - (v)iuvo - (d)ivorciado: ')

    civil_lista = ['s', 'c', 'v', 'd']
    sexo_lista = ['m', 'f']

    if len(nome) < 3:
        print(f'O nome {nome} é muito pequeno')
        continue
    if not idade.isdigit():
        print('Digite um numero de idade valido')
        continue
    else:
        idade = int(idade)
        if idade < 0 or idade > 150:
            print(f'A idade {idade} é invalido')
            continue
    if not salario.isdigit():
        print('Digite  um valor de salario valido')
        continue
    else:
        salario = float(salario)
        if salario < 0:
            print('Digite um valor salario correto')
            continue

    if sexo.lower() not in sexo_lista:
        print('O sexo não é valido')
        continue

    if civil.lower() not in civil_lista:
        print('O estado civil digitado não é correto')
        continue

    print(f'Seu nome é {nome}\n'
          f'Sua idade é: {idade}\n'
          f'Seu salario é: {salario:.2f}\n'
          f'Seu sexo é: {sexo}\n'
          f'Seu estado civil é: {civil}')
    break




