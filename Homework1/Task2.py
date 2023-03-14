print("Сколько журавликов сделали дети")
quantity = int(input())
count = quantity / 6
if quantity%6 == 0:
    print(f"Петя и Сережа сделали по {int(count)} журавликов")
    print(f"Катя сделала {int(count)*4} журавликов")
else:
    print("Вы ошиблись ")
