dig_str = ''
while 1:
    dig = input('input digit: ')
    if dig.lower() == 'stop':
        break
    elif dig.isdigit():
        dig_str += dig
        integer = int(dig_str)
    else:
        print(dig, 'is not a digit')
print('you input "stop"')
print(f'your integer is {integer}')
