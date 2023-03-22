"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
 Faça um programa que gere a série até que o valor seja maior que 500.

"""

fibo = [1]

a = 1

for i in range(1, 1001):
    if fibo[i-1] >= 500:
        break
    else:
        print(fibo[i-1])
        fibo.append(a)
        a = fibo[i-1] + a

