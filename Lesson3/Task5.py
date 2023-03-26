# Дана упорядоченная последовательность an чисел от 1 до N.
# Из копии данной последовательности bn удалили одно число,
# а оставшиеся перемешали. Найти удаленное число.
import random

n = int(input("Введите длину последовательности "))

numb_list = []
for i in range(n + 1):
    numb_list.append(i)

print(numb_list)
set1 = set(numb_list)                                    # перевели в множество
numb_list.pop(int(input("Какой элемент удалить? ")))

random.shuffle(numb_list)
print(numb_list)

set2 = set(numb_list)                                      # перевели в множество после удаления
print(set1.difference(set2))                               # нашли разницу

