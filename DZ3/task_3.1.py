#### 3.1[16]: Дан список целых чисел.  Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.

x = int(input("Введите число: "))
count=0
List_1=[0, 4, 8, 12, 3, 9, 4, 13, 4]
for i in range(len(List_1)):
    if List_1[i] == x:
        count +=1
if count > 0:
    print(f'Число"{x}" встречается {count} раз/а в списке')   
else:
    print('-1')
        
