# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text))  # 39  позволяет узнать размер нашей строки
# print('ещё' in text)  # True  есть ли слово еще в нашей строке
# print(text.lower())  # съешь ещё этих мягких французских булок
# print(text.upper())  # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# print(text.replace('ещё', 'ЕЩЁ'))  # СъЕШЬ ЕЩЁ этих МяГкИх французских булок 1 арг что мы меняем 2 арг на что мы меняем

text = 'съешь ещё этих мягких французских булок'
print(text[0])  # c
print(text[1])  # ъ
print(text[len(text) - 1])  # к  или text[-1] без лен
print(text[-5])  # б
print(text[:])  # съешь ещё этих мягких французских булок
print(text[:2])  # съ

print(text[len(text) - 2:])  # ок
print(text[2:9])  # ешь ещё
print(text[6:-18])  # ещё этих мягких
print(text[0:len(text):6])  # сеикакл будет вывод каждый 6 элемент
print(text[::6])  # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ...