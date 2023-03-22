nome=input('Difite o nome do funcionario:\n')
sal=float(input('Digite o Salario do funcionario:\n'))

if sal <= 280:
    print('O aumento do ',nome,' é de;\n', sal+(sal*0.2),'\nO valor do aumento é: ', sal*0.2)

elif sal > 280 and sal <= 700:
    print('O aumento do ',nome,' é de;\n', sal+(sal*0.15),'\nO valor do aumento é: ', sal*0.15)

elif sal > 700 and sal <= 1500:
    print('O aumento do ',nome,' é de;\n', sal+(sal*0.1),'\nO valor do aumento é: ', sal*0.1)

elif sal > 1500:
    print('O aumento do ',nome,' é de;\n', sal+(sal*0.05),'\nO valor do aumento é: ', sal*0.05)

else:
    print('valor incorreto')