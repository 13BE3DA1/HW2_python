x = int(input())
# начинаем цикл c двойки так как это минимальный делитель:
for i in range (2,x):
    # ищем первое число которое нацело делит x:
    if x % i == 0:
        print (i)
        break