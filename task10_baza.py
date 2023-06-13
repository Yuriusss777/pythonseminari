coins = int(input("Введите количество монет: "))
count_zero = 0
count_one = 0
for i in range(coins):
    x = int(input("укажите сторону монету где 1 - решка, а 0 - герб: "))
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
    if count_one > count_zero:
        print(count_zero)
    else:
        print(count_one)
