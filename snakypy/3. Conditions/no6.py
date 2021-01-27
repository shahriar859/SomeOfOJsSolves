c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

if c1%2 == r1%2:
    a = 1
else:
    a = 2
if c2%2 == r2%2:
    b = 1
else:
    b = 2
if a==b:
    print('YES')
else:
    print('NO')
