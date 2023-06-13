sum_1 = int(input("Введите сумму двух чисел: "))
sum_2 = int(input("Введите произведение двух чисел: "))
for i in range(sum_1):
    for j in range(sum_2):
        if sum_1 == i + j and sum_2 == i * j:
            print(i, j)
