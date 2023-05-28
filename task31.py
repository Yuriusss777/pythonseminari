# Последовательностью фибоначчи называется последовательность чисел  a0 , a1 , ..., an , где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию


def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


print(fibo(8))
