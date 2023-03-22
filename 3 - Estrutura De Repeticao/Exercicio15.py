"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o
n−ésimo termo.
"""
fibo = [1]

a = 1

for i in range(1, 1001):
    print(fibo[i-1])
    fibo.append(a)
    a = fibo[i-1] + a