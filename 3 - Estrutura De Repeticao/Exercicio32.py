num = int(input('Digite um numero: '))
fat = 1

print(f'\nFatorial de: {num}\n'
      f'{num}! =', end=' ')

for i in range(num, 0, -1):
    if i > 1:
        print(i, end= ' . ')
    fat = i * fat

print('1 = ', fat)