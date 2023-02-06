# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# 2
import random

n = int(input("Введите числоот 1 до 100:"))
items = [random.randint(0, 1) for i in range(n)]
print(items)
count1 = 0
count2 = 0

for i in range(len(items)):
    if items[i] == 1:
        count1 = count1 + 1
    else:
        count2 = count2 + 1

if count1 < count2:
    print(count1)
else:
    print(count2)
