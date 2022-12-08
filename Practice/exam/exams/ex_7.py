# Написать функцию copyfile: функция принимает два аргумента –
# имена файлов source и destination, открывает source, читает его,
# открывает destination, пишет в него.
# Если source не найден или destination уже существует,
# то выбрасываются соответствующие исключения.
# Нужно проверить выполнение функции как для правильных аргументов, так и для приводящих к исключениям. (3 балла)

def copyfile(source, destination):
    try:
        with open(source, 'r') as s, open(destination, 'x') as w:
            s_read = s.read()
            w_write = w.write(s_read)
            return w_write
    except FileNotFoundError:
        return "File doesn't exist"
    except FileExistsError:
        return "File already exist"


text = copyfile('hello.txt', 'new_file.txt')
