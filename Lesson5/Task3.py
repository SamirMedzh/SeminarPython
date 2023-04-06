# Вводится слово и определяется кол-во очков в слове

my_dict = {1: 'AEIOULNSTRАВЕИНОРСТ',
           2: 'DGДКЛМПУ',
           3: 'BCMPБГЁЬЯ',
           4: 'FHVWYЙЫ',
           5: 'KЖЗХЦЧ',
           8: 'JXШЭЮ',
           10: 'QZФЩЪ'}

total = 0
word = input('Введите слово: ')
for letter in word:
    for key, value in my_dict.items():
        if letter.upper() in value:
            total += key

if all(list(map(lambda x: 64 < ord(x) < 123, word))):
    print(f'Английское слово "{word}" весит {total} баллов')
elif all(list(map(lambda x: 1039 < ord(x) < 1104, word))):
    print(f'Русское слово "{word}" весит {total} баллов')
else:
    print('Ты читер! Можно использовать только один алфавит')




