# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю
# последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

list_len = int(input("Введите длину последовательности: "))
shift = int(input("Введите величину сдвига: "))

list = [_ for _ in range(list_len)]
print(list)

# for i in range(shift):                 # 1 решение
#     list.insert(0, list.pop())
# print(list)

# print(list[-shift:] + list[:-shift])   # 2 решение срезом

for i in range(len(list)):
    print(list[i - shift], end=" ")   # 3 решение
