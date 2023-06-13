n = int(input("Введите шестизначный номер билета: "))
n1 = int(n / 100000)
n2 = int((n / 10000) % 10)
n3 = int((n / 1000) % 10)
n4 = int((n / 100) % 10)
n5 = int((n / 10) % 10)
n6 = int(n % 10)

summa1 = n1 + n2 + n3
summa2 = n4 + n5 + n6

if summa2 == summa1:
    print("yes")
else:
    print("no")
