# Дан массив, состоящий из целых чисел. Напишите программу,
# которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного

from random import randint
print('Введите длину списка (> 3) и диапазон ')
my_vars = list(map(int, input('Введите числа через пробел -> ').split()))
my_list = [randint(my_vars[1], my_vars[2]) for _ in range(my_vars[0])]
print(my_list)
k = 0
for i in range(1, my_vars[0] - 1):
    if my_list[i - 1] < my_list[i] > my_list[i + 1]:
        k += 1
print(k)


