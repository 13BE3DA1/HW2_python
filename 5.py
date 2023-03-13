maxx = 0
count = 0
while True:
    vvod = int(input())
    if vvod == 0: break
    # если vvod больше чем maxx то maxx присваивам значение vvod и результат будет = 1:
    if vvod > maxx:
        maxx = vvod
        count =1
    # если vvod = maxx то результат всегда будет +1 за каждое одинаковое значение:
    elif vvod == maxx:
        count += 1
print(count)