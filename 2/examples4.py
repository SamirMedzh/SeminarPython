# Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. В словаре для определения
# элемента используется значение ключа (строка, число)
d = {}
d = dict()
d["w"] = "qwerty"
print(d)

d["q"] = "werty"
print(d)
print(d["w"])
# dictionary = {}  # создание пустого словаря
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента

for item in dictionary:
    #print("{} : {}".format(item, dictionary[item]))
    print(item)

for (k, v) in dictionary.items():   # можно так записать
    print(k, v)
