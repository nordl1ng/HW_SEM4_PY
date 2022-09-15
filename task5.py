# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import re
import itertools

with open('pol1.txt', 'r') as f:
    pol1 = f.read()
    print(pol1)

with open('pol2.txt', 'r') as f:
    pol2 = f.read()
    print(pol2)

k = int (pol1[5])
print(k)

pol1 = pol1.replace('= 0', '')
pol1 = pol1.replace("x +", "x^1 +")
pol1 = re.sub("[*|^| ]", " ", pol1).split('+')

pol2 = "22*x^3 + 93*x^2 + 62*x + 95 = 0"
pol2 = pol2.replace('= 0', '')
pol2 = pol2.replace("x +", "x^1 +")
pol2 = re.sub("[*|^| ]", " ", pol2).split('+')

pol1_list=[]
pol2_list=[]

for i in range (0,len(pol1)):
    pol1_list.append(pol1[i].split("x"))

for i in range (0,len(pol2)):
    pol2_list.append(pol2[i].split("x"))

pol1_list_int=[]
for i in range (0,len(pol1)):
    pol1_list_int.append([int(item) for item in pol1_list[i]])
pol2_list_int=[]
for i in range (0,len(pol2)):
    pol2_list_int.append([int(item) for item in pol2_list[i]])

pl1=str(pol1_list_int)
pl1=re.sub("]", "", pl1)
pl1=re.sub("[ [ ]", "", pl1)
pl1_int = pl1.split(",")

for i in range (0,len(pl1_int)):
    pl1_int[i]=int(pl1_int[i])
print(pl1_int)

pl2=str(pol2_list_int)
pl2=re.sub("]", "", pl2)
pl2=re.sub("[ [ ]", "", pl2)
pl2_int = pl2.split(",")
for i in range (0,len(pl2_int)):
    pl2_int[i]=int(pl2_int[i])
print(pl2_int)

summ = []
for i in range (0,len(pl1_int)):
    if i == 0 or i % 2 ==0:
        summ.append(pl1_int[i]+pl2_int[i])

summ.reverse()

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
    
print( poly (k, summ))

f1 = open('pol3.txt', 'w')
f1.write(poly (k, summ))
f1.close()
