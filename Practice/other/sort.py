a = [0, 7, 23, 18, 2, 5, -5, 0, 2, 11, 3, 7, 1]
b = []

# 1
check_border = len(a)
while check_border > 0:
    check_part = a[:check_border]
    min_checked = min(check_part)
    a.append(min_checked)
    a.remove(min_checked)
    check_border -= 1
print(a)

# 2
while len(a) > 0:
    value_min = min(a)
    b.append(value_min)
    a.remove(value_min)
print(b)

# 3
while len(a) > 0:
    value_min = a.pop(a.index(min(a)))
    b.append(value_min)
print(b)