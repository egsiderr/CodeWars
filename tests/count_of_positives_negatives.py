"""Дан массив целых чисел.
Верните массив, в котором первый элемент - счетчик положительных чисел,
а второй - сумма отрицательных чисел. 0 не является ни положительным, ни отрицательным числом.
Если входной массив пуст или равен null, возвращается пустой массив."""

def count_positives_sum_negatives(arr):
    if arr is None:
        return []
    elif len(arr) == 0:
        return []

    pos_count = 0
    neg_count = 0
    for i in arr:
        if i > 0:
            pos_count = pos_count + 1
        elif i < 0:
            neg_count = neg_count + i
    result = [pos_count, neg_count]
    return result

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
