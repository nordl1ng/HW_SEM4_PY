# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('pol1.txt', 'r') as f:
    pol1 = f.read()
    print(pol1)

with open('pol2.txt', 'r') as f:
    pol2 = f.read()
    print(pol2)

pol1_list=pol1.split("+")
print(pol1_list)
pol2_list=pol2.split("+")
print(pol2_list)

print(f"Элементов1: {len(pol1_list)}")
print(f"Элементов2: {len(pol2_list)}")

from operator import contains
import re
pol1_list_r1 = []
for i in range (0,len(pol1_list)):
    pol1_list_r1.append(re.findall(r'\d+', pol1_list[i]))

pol1_list_r2 = []
for i in range (0,len(pol2_list)):
    pol1_list_r2.append(re.findall(r'\d+', pol2_list[i]))

print(pol1_list_r1)
print(pol1_list_r2)

if pol1_list_r1 contains ",":
    