# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

listt=input(("Введите элементы массива через пробел:")).split(" ")
list_int=[int(item) for item in listt]
print(f"Заданный список: {list_int}")

def repeat(list):
    listt2 = []
    for i in range (0,len(list)):
        count=0
        for k in range (0,len(list)):
            if i!=k and list[i]==list[k]:
                count += 1
        if count ==0:
            listt2.append(list[i])
    print(f"Не повторяющиеся элементы: {listt2}")
    
repeat(list_int)
