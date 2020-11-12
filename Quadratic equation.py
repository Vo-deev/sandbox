print('Input 3 numbers')
a, b, c = float(input()), float(input()), float(input())
from math import *
d = b ** 2 - 4 * a * c
if d < 0:
    print('Нет корней')
elif d == 0:
    x1 = b / (2 * a) * (-1)
    print(x1)
elif d > 0:
    x1 = ((-1) * b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = ((-1) * b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))