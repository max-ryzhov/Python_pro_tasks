import multiprocessing


def sum_type(*args):
    for i in range(1, len(args)):
        if not isinstance(args[i], type(args[0])):
            return 'Different type of arguments'
        break

    for j in range(1, len(args)):
        sum_args = args[0]
        sum_args += args[j]
        return sum_args


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=sum_type, args=(1, 2, 3, 4, 5))
    p2 = multiprocessing.Process(target=sum_type, args=('a', 'b', 'c'))
    p3 = multiprocessing.Process(target=sum_type, args=([1, 2], ['a', 'b']))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print(p1)
    print(p2)
    print(p3)
    print('all processes are finished')
