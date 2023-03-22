try:
        nota1=int(input('Digite a nota do aluno:\n'))
        nota2=int(input('Digite a nota do aluno:\n'))

        media=(nota1+nota2)/2

        while nota1 > 10 or nota2 > 10:
            print('Não pode haver valores maiores que "10"')

            nota1=int(input('Digite a nota do aluno:\n'))
            nota2=int(input('Digite a nota do aluno:\n'))

            media=(nota1+nota2)/2

        else:
            media=(nota1+nota2)/2
            if media >= 7 and media <= 9:
                print('Aprovado')

            elif media == 10:
                print('Aprovado com louvor')

            elif media >= 0 and media <= 6:
                print('reprovado')

            else:
                    print('valor incorreto') 
except:
    print('valor incorreto')
