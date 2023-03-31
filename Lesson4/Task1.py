# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов добавляется
# к символам с помощью постфикса формата _n.


# input_str = input("Введите строку: ")
#
# dict_1 = {"v": "3"}
#
# for i in input_str:
#     if i in dict_1:
#         print(f"{i}_{dict_1[i]}", end=" ")
#         dict_1[i] += 1
#     else:
#         dict_1[i] = 1
#         print(i, end=" ")

#  2 решение
import random
import string

my_string =''.join([random.choice(string.ascii_letters) for _ in range(30)])
# choice   выводит случайные
# srring.ascii_letters выводит англ алфавит большие и маленькие буквы

dict = {}
for char in my_string:
    dict[char] = dict.get(char, 0) + 1
    if dict.get(char) > 1:
        print(f'{char}_{dict.get(char)}', end=' ')
    else:
        print(char, end='')

