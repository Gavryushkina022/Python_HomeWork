# Задача 18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5
from random import randint

number = int(input("Введите количество элементов массива "))
list_1 = [1] * number

for i in range(number):
    list_1[i] = randint(1, 10)
print(list_1)
x = int(input("Введите число для поиска ближайшего к нему "))
dif = 0
while True:
    if x - dif in list_1 and x + dif in list_1 and x - dif != x + dif:
        print(x + dif, x - dif)
        break
    elif x - dif in list_1:
        print(x - dif)
        break
    elif x + dif in list_1:
        print(x + dif)
        break
    else:
        dif += 1
if x in list_1:
    print("Такое число уже есть в списке")
