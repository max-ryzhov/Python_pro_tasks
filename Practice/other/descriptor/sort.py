# Сортировка:

a = [1, 57, 33, 2, 7, 99]

# С помощью функции sorted
b = sorted(a)
print(b)

# с помощью метода списков lst.sort()
a.sort()
print(a)

# list.sort() - для списков
# sorted() - работает со всем
# и итерируемыми объектами. пр - множества, ?кортежи?

# f = open('max.txt', 'r+')
# res = f.read()
# print(res)
# f.close()

# !!! при вызове функции read нужно ограничивать размер чтения.
# иначе может чего лишнего считать
i = 0
f = open('max.txt', 'w')
while i < 100:
    f.write(f'{i} пряничные человечки \n')
    i = i + 1
f.close()

