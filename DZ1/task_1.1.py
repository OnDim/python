#### 1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод

n = int(input())
number = str(n)
result = 0
while n != 0:
    temp = n % 10
    result += temp
    n //= 10
print(f'Сумма чисел числа {number} равна {result}')
