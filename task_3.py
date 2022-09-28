# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

import random

import random

items = [random.randint(0, 10) for i in range(20)]
print(items)
print(list(set(items)))

