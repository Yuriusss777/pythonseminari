# дан список чисел, определите, сколько в нем встречается различных
# чисел: [1, 1, 2, 0, -1, 3, 4, 4]  ответ 6

lst = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(lst)))

# lst = [1, 1, 2, 0, -1, 3, 4, 4]
# i = 1
#
# for index in range(len(lst) - 1):
#     if lst[index] == lst[index + 1]:
#         continue
#     else:
#         i += 1
#
# print(i)
