from geometor.utils import *
from geometor.model import *
from geometor.render import *
from itertools import permutations

class Line(spg.Line):
    def __init__(self, pt1, pt2):
        super().__init__(pt1, pt2)

A = point(0,0)
B = point(1,0)

l1 = Line(A, B)


print(l1.func)
