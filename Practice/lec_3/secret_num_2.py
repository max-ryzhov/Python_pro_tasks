import random

min_border = int(input('введите минимальное значение: '))
max_border = int(input('введите максимальное значение: '))

secret = random.randint(min_border, max_border)
print(secret)

while 1:
    guess = input('введите предполагаемое число: ')
    if not(guess.isdigit()):
        print(f'{guess} - это не число')
        break
    guess = int(guess)
    if guess == secret:
        print(f'угадал - {guess}')
        break
    if guess > secret:
        print('загаданное число меньше')
        continue
    elif guess < secret:
        print('загаданное число больше')
        continue





# while not((guess == secret) and (not secret.isdigit())):