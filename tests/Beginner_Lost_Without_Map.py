"""Если задан массив целых чисел, верните новый массив, в котором каждое значение удвоено.
Например:
[1, 2, 3] --> [2, 4, 6]"""

def maps(a):
    return list(map(lambda x: x * 2, a))

print(maps([1, 2, 3]))