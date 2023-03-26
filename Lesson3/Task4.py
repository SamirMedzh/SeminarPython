# Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)

from random import randint

my_list = [randint(0, 10) for _ in range(5)]
count = 0
for i in range(1, len(my_list)):
    if my_list[i - 1] < my_list[i]:
        count += 1
print(my_list)
print(count)

new_list = [i for i in range(1, len(my_list)) if my_list[i - 1] < my_list[i]]  # 2 решение лист комприхейшн
print(my_list)
print(len(new_list))

