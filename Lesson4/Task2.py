# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов
# идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.

# input_str = input("Введите строку: ").lower()
#
# strings = input_str.split()
#
# set_1 = set()
#
# for i in range(0, len(strings)):
#     if strings[i] not in set_1:
#         set_1.add(strings[i])
#
#
# print(set_1)
# print("Уникальных слов введено: ", len(set_1))

# 2 решение

input_str = input("Введите строку: ")

print(len(set(input_str.replace('.','').lower().split())))
