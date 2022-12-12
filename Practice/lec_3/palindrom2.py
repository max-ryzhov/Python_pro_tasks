string = input('Input word: ')


def is_palindrom(word):
    len_w = len(word)
    half_len = len_w // 2
    first_part = word[0:half_len]
    if len_w % 2:
        second_part = word[(half_len+1):(len_w+1)]
    else:
        second_part = word[half_len:(len_w+1)]
    if first_part == second_part[::-1]:
        return 'palindrom'
    else:
        return 'nixya'


res = is_palindrom(string)
print(res)