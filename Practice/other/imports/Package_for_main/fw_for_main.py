from math import sqrt


class RightTriangle:
    def __init__(self, cat1=None, cat2=None, hyp=None):
        self.cat1 = cat1
        self.cat2 = cat2
        self.hyp = hyp

    def hypotenuse(self):
        hyp = sqrt(self.cat1 ** 2 + self.cat2 ** 2)
        return hyp
