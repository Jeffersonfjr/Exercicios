#  O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#  • Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#  • entre 3 e 4 como "Cúmplice"
#  • E 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perg1 = int(input('Telefonou para a vítima?\n1 - Sim\n2 - Não\n'))
perg2 = int(input('Esteve no local do crime?\n1 - Sim\n2 - Não\n'))
perg3 = int(input('Mora perto da vítima?\n1 - Sim\n2 - Não\n'))
perg4 = int(input('Devia para a vítima?\n1 - Sim\n2 - Não\n'))
perg5 = int(input('á trabalhou com a vítima?\n1 - Sim\n2 - Não\n'))

resp1 = 'Inocente'

if perg3 == 1 or perg4 == 1:
    resp1 = 'Cúmplice'
if perg2 == 1:
    resp1 = 'Suspeito'
if perg5 == 1:
    resp1 = 'Assassino'

print('Você é ', resp1)
