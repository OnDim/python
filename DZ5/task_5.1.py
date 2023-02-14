#### 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения. Циклы использовать нельзя

# Примеры/Тесты:
#    <function_name>(2,0) -> 1
#    <function_name>(2,1) -> 2
#    <function_name>(2,3) -> 8
#    <function_name>(2,4) -> 16

def power(base, exp):
    if (exp == 0):
        return (1)
    if (exp == 1):
        return (base)
    if (exp > 1):
        return (base *power(base, exp-1))
print("Результат возведения в степень равен:", power(2, 4))