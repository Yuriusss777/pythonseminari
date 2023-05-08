revenue = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
finResult = revenue - costs
print(f'Финансовый результат - прибыль. Ее величина: {finResult}')
profit = finResult / revenue
print(f'Рентабельность выручки = {profit}')
staff = int(input("Введите численность сотрудников фирмы: "))
profitStaff = finResult / staff
print(f'прибыль фирмы на одного сотрудника = {profitStaff}')
