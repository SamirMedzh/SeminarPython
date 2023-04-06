def list_sum(numb: int):
    if numb == 0:            # словие выхода
        return numb
    return numb + list_sum(numb - 1)     # сама рекурсия
print(list_sum(6))