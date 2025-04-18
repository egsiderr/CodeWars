"""Реализуйте функцию, принимающую 3 целых значения a, b, c.
Функция должна возвращать true, если треугольник может быть построен со сторонами заданной длины,
и false в любом другом случае.
(В этом случае все треугольники должны иметь площадь больше 0, чтобы быть принятыми).
Примеры:

Вход -> Выход
1,2,2 -> true
4,2,3 -> true
2,2,2 -> true
1,2,3 -> false
-5,1,3 -> false
0,2,3 -> ложь
1,2,9 -> ложь"""

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(is_triangle(-5,1,3))