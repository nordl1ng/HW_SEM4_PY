# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input("Введите k: "))

def randomlist (k):
    list = []
    for i in range(0, k+1):
        list.append(str(random.randint(0, 100)))
    return list

def poly (k, list):
    str_p = ""
    for i in range(k, -1, -1):
        if i != 0:
            if i != 1:
                if list[i] != 0 and list[i] != 1:
                    str_p += f"{list[i]}*x^{i} + "
                elif list[i] == 1:
                    str_p += f"x^{i} + "
                else:
                    str_p += ""
            if i == 1:
                if list[i] != 0 and list[i] != 1:
                    str_p += f"{list[i]}*x + "
                elif list[i] == 1:
                    str_p += f"x + "
                else:
                    str_p += ""
        else:
            if list[i] != 0:
                str_p += f"{list[i]} = 0"
            else:
                print(len(str_p))
                str_p = str_p[:len(str_p)-2]
                str_p += f"= 0"
    return str_p

list1 = randomlist (k)
list2 = randomlist (k)
poly (k, list1)
print (poly (k, list1))
poly (k, list2)
print (poly (k, list2))


f1 = open('pol1.txt', 'w')
f1.write(poly (k, list1))
f1.close()

f2 = open('pol2.txt', 'w')
f2.write(poly (k, list2))
f2.close()