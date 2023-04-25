lShoco = int(input("Введите длину шоколадки: "))
bShoco = int(input("Введите ширину шоколадки: "))
dShoco = int(input("Введите требуемое количество долек для разлома "))

if (dShoco / lShoco) == (dShoco // lShoco):
    print(f"Да, можно отломить {dShoco} дольки")
elif (dShoco / bShoco) == (dShoco // bShoco):
    print(f"да, можно отломить {dShoco} дольки")
else:
    print(f"нет, нельзя отломить {dShoco} дольки")
