# ordered or not (from right to left)
n = int(input())
flag = True
ld = n % 10
while n != 0:
    num = n % 10
    if ld > num:
        flag = False
    num, ld = ld, num
    n = n // 10
if flag == True:
    print('YES')
else:
    print('NO')