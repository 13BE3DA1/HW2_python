x = int(input())
for i in range(x):
    # создаём переменную y:
    y = int(input())
    # если y = 0 в таком случае код выдаёт 'yes':
    if y == 0:
        print('YES')
        break
# в случе если y не ровняется 0 код выдаёт 'no':
else:
    print ('NO')