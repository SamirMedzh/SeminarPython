# Дан список чисел. Определите, сколько в нем встречается различных чисел

import random

# создаем список
numb_list = [random.randint(0,20) for _ in range(20)]
print(numb_list)
print(type(numb_list))

# переводим в множество т.к. оно хранит только уникальные числа
numb_set = set(numb_list)
print(numb_set)
# ри помощи функции len находим кол-во
print(len(numb_set))
