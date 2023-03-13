x = int(input())
y = int(input())
n = 1
m = 1
while 0 == 0:
    if x == 0:
        break
    if y == 0:
        break
    while x > y:
        if y == 0:
            break
        n += 1
        if n > m:
            m = n
            x = y
            y = int(input())
        else:
            x = y
            y = int(input())
    n = 1
    while x < y:
        n += 1
        if n > m:
            m = n
            x = y
            y = int(input())
        else:
            x = y
            y = int(input())
    n = 1
    while x == y:
        n = 1
        x = y
        y = int(input())
print(m)


