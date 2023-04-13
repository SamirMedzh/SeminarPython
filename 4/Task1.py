def calk1(a, b):
    return a * b


def math(op, x, y):
    print(op(x, y))

# def calk2(a, b):
#     return a + b

calk2 = lambda a, b: a + b

math(calk2, 5, 45)