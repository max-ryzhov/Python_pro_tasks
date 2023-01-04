num = 'a'
while not(num.isdigit() and len(num) == 5):
    num = input('Введите пятизначное число: ')

num = int(num)    # введенную строку явно в число
digit_list = list(str(num))    # число в список поэлементно
number = 1
for i in digit_list:
    print(f'{number}-я цифра = {i}')
    number += 1
