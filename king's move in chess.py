print('Input twice numbers from 1 to 8')
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
    print('YES')
else:
    print('NO')