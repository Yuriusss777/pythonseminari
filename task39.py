# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)
# Вывод:3 3 2 12

# n = int(input("Введите количество элементов первого массива: "))
# first_lst = [int(input("Введите номер: ")) for el in range(n)]
#
# m = int(input("Введите количество элементов второго массива: "))
# second_lst = [int(input("Введите номер: ")) for el in range(m)]
first_lst = [3, 1, 3, 4, 2, 4, 12]
second_lst = [4, 15, 43, 1, 15, 1]
new_lst = []
for number in first_lst:
    if number not in second_lst:
        new_lst.append(number)
print(new_lst)

new_lst = [number for number in first_lst if number not in second_lst]
print(new_lst)