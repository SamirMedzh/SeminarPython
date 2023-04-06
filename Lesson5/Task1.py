import random

my_list = [random.randint(0, 5) for _ in range(20)]
print(my_list)
number = int(input("Введите искомое число: "))
print(f'Число {number} встречается в списке {my_list.count(number)} раз')