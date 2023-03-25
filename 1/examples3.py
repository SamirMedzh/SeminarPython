# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter = 5 # iter = iter  5

a = 1 > 4
print(a) # False
# —------------------------------------
a = 1 < 4 and 5 > 2
print(a) # True
# —------------------------------------
a = 1 == 2
print(a) # False
# —------------------------------------
a = 1 != 2
print(a) # True
# #Можно сравнивать не только числовые значения, но и строки:
# a = 'qwe'
# b = 'qwe'
# print(a == b) # True
# #В Python можно использовать тройные и даже четверные
# #неравенства:
# a = 1 < 3 < 5 < 10
# print (a) # True