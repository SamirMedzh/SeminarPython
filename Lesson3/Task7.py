aa = 5
bb = aa
print(id(aa))     # место в памяти одинаковое
print(id(bb))
aa = aa + 1       # Здесь мы не изменили а создали новый
print(aa)
print(bb)
print(id(aa))     # место в памяти разное
print(id(bb))


