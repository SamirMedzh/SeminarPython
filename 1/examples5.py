# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(-5, 0) # ----
# r = range(1, 10, 2) # 1 3 5 7 9
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
# print(i)
# # 100 80 60 40 20

# for i in 'qwerty':
#  print(i)

line = ""  # переменная которая является пустой строкой
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

