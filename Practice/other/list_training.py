lst1 = [1, 2, 3, 4, 5]
lst2 = [x for x in range(1, 11)]
lst3 = list('hello mather fucker')

a = dict(one=1, two=2, three=3)     # словарь

a2 = dict([('one', 1)])

b = {'one': 1, 'two': 2, 'three': 3}    # словарь
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))    # ?
d = dict([('two', 2), ('one', 1), ('three', 3)])    # словарь
e = dict({'three': 3, 'one': 1, 'two': 2})    # словарь

print(a, type(a))

print(a2, type(a2))

print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))




