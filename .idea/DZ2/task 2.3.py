####  2.3[14]: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

N = int(input())
i = 0
while 2 ** i < N:
    print(2 ** i, end=' ')
    i += 1