import math


def pythagoras(a, b):
    a2 = a ** 2
    b2 = b ** 2
    c2 = a2 + b2
    c = math.sqrt(c2)
    return c


print(pythagoras(3, 4))
