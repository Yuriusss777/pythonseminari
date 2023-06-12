# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10 в 5-й степени
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:
# 300
# Вывод:
# 220 284

def get_sum(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s


# print(get_sum(284))

def frendl(k):
    res = []
    for n in range(1, k):
        if n not in res:
            m = get_sum(n)
            if n == get_sum(m) and n != m:
                res.append(n)
                res.append(m)
    return res


print(frendl(300))