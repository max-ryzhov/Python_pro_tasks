# Написать функцию count_symbol: считает сколько раз символ встречается в строке. (3 балла)
# оставил сравнение с учетом регистра по умолчанию
def count_symbol(string, symbol):
    count = 0
    for i in string:
        if i == symbol:
            count += 1
    return count


n = count_symbol('Hi, Elvis, I am here!', 'i')
print(n)

