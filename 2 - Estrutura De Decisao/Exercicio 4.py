v=input('Digite uma letra: ')

if v in "aeiou":
    print('Sua letra é uma vogal')

elif v in "bcdfghjlmnpqrstvxywz":
    print('Sua letra é uma consoante')

else:
    print('Você não digitou uma letra.')