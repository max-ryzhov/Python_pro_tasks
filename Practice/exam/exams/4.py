import math


class SimpleInt:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.s = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.s < self.m:
            self.lst = []
            count = 2
            i = 0
            while i <= self.m:
                prime = True
                for x in range(2, int(math.sqrt(count) + 1)):
                    if count % x == 0:
                        i += 1
                        prime = False
                        break
                if prime:
                    self.lst.append(count)
                count += 1
                self.s += 1
            return self.lst
        else:
            raise StopIteration


for i in SimpleInt(100, 1):
    print(i)







# def main(m):
#     lst = []
#     count = 2
#     i = 0
#     while i <= m:
#         prime = True
#         for x in range(2, int(math.sqrt(count) + 1)):
#             if count % x == 0:
#                 i += 1
#                 prime = False
#                 break
#         if prime:
#             lst.append(count)
#         count += 1
#     return lst
#
#
# p = main(5)
# print(p)
#
