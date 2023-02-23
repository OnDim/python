#### 6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :
# - Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#	Напишите функцию
#	- Аргументы: три указанных параметра
#	- Возвращает: список элементов арифмитической прогрессии.

a1, d, n = [int(el) for el in input("Введите a1, d, n: ").split()]

def arithmetic_progression(start, step, quantity):
    return[start+step*idx for idx in range(quantity)]

print(arithmetic_progression(a1, d, n)) 

# ```(*)``` **Усложнение.** Для формирования списка внутри функции используйте Comprehension

new_lst=[a1 + d * i for i in range(n)]
print(new_lst)

# ```(**)``` **Усложнение.** Присвоение значений переменным a1,d,n запишите, используя только один input,
# в одну строку, вам понадобится распаковка и Comprehension или map

my_lst=int(input("Введите a1, d, n: ")) 
type(my_lst)
var=[*my_lst]
new_lst=[var[1] + var[2] * i for i in range(var[3])]
print(my_lst)


