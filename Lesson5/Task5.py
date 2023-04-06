# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# 0, 1 ,1, 2, 3, 5, 8, 13, 34, 55, 89

def fib(numb):
    if numb == 1 or numb == 0:
        return 1
    return fib(numb - 1) + fib(numb - 2)


print(fib(5))
