loginc = 'jeff'
senhac = '123456'

login = input('Digite sue login:\n')
senha = input('Digite sua senha:\n')

while login != loginc and senha != senhac:
    print('Login/Senha incorreto, digite novamente!\n')
    login = input('Digite sue login:\n')
    senha = input('Digite sua senha:\n')

else:
    print('Login realizado com sucesso.')


