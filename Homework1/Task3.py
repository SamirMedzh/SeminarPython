# билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# # Вам требуется написать программу, которая проверяет счастливость билета.

print("Введите 6-значное число ")
luckynumber = int(input())
numb1 = luckynumber // 100000
numb2 = (luckynumber//10000) % 10
numb3 = (luckynumber//1000) % 10
numb4 = (luckynumber//100) % 10
numb5 = (luckynumber//10) % 10
numb6 = luckynumber % 10

if luckynumber > 100000 and luckynumber < 1000000:
    if numb1 + numb2 + numb3 == numb4 + numb5 + numb6:
        print("Это счастливый билет")
    else:
        print("Это несчастливый билет")
else:
    print("Вы ошиблись ")

