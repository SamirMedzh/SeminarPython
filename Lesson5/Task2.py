import random

my_list = [random.randint(0, 100) for _ in range(20)]
print(my_list)

number = int(input("Введите число: "))
nearest_number = my_list[0]
dist = abs(number - nearest_number)

for num in my_list:
    if abs(num - number) < dist:
        dist = abs(num - number)
        nearest_number = num

print(f'Ближайшее число к {number} является {nearest_number}')