try:
    nome=input('Insira o nome do Aluno: ')
    n1=int(input('Insira a primeira nota do Aluno: '))
    n2=int(input('Insira a segunda nota do Aluno: '))
    n3=int(input('Insira a terceira nota do Aluno: '))
    n4=int(input('Insira a quarta nota do Aluno: '))

    print('A nota do',nome,'é: ', (n1+n2+n3+n4)/4)

except:
    print('Ha valores incorretos, favor verifique')