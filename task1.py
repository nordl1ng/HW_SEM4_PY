# 1. Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141

import random
a = random.uniform(0.0, 100.0)
print(f"Заданное число: {a}")
acc=(input("задайте точность: "))
print(round(a,len(acc)-2))