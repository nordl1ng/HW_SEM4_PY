# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

n = int(input("Введите N: "))
lst = []
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            # если делитель найден, число не простое.
            break
    else:
        lst.append(i)
print(lst)
lst2 = []

for i in range(0,len(lst)):
    if n % lst[i] == 0:
        lst2.append(lst[i])
print(f"Список натуральных множителей {lst2}")