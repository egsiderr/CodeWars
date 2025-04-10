"""Напишите функцию, которая принимает массив чисел (целые числа для тестов) и целевое число.
Она должна находить в массиве два разных элемента, которые при сложении дают целевое значение.
Индексы этих элементов должны быть возвращены в виде кортежа/списка
(в зависимости от языка), например: (index1, index2).
Для целей этого ката некоторые тесты могут иметь несколько ответов;
принимаются любые правильные решения.
Входные данные всегда будут корректными (числа будут представлять собой массив длины 2 или больше,
и все элементы будут числами; цель всегда будет суммой двух различных элементов из этого массива).

two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)
two_sum([3, 2, 4], 6) # returns (1, 2) or (2, 1)"""

def two_sum(numbers, target):

    # for i in numbers:
    #     for x in numbers:
    #         if i + x == target and numbers.index(i) != numbers.index(x):
    #             print([numbers.index(i), numbers.index(x)])
    #
    # return numbers.index(i), numbers.index(x)

    for i, num1 in enumerate(numbers):
        for x, num2 in enumerate(numbers):
            if i != x and num1 + num2 == target:
                return (i, x)

print(two_sum([1, 2, 3], 4))
