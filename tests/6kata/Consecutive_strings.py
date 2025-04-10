"""
Вам дан массив (список) строк strarr и целое число k.
Ваша задача - вернуть первую самую длинную строку, состоящую из k последовательных строк, взятых в массиве.
Примеры:
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
Конкатенируем последовательные строки strarr на 2, получаем:
treefoling (длина 10) конкатенация strarr[0] и strarr[1]
folingtrashy (" 12) конкатенация strarr[1] и strarr[2]
trashyblue (" 10) конкатенация strarr[2] и strarr[3]
blueabcdef (" 10) конкатенация strarr[3] и strarr[4]
abcdefuvwxyz (" 12) конкатенация strarr[4] и strarr[5]

Две строки являются самыми длинными: «folingtrashy» и «abcdefuvwxyz».
Первой пришла "folingtrashy", поэтому
longest_consec(strarr, 2) должна вернуть "folingtrashy".

Аналогично:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
n - длина массива строк, если n = 0 или k > n или k <= 0, верните "" (верните Nothing в Elm, "nothing" в Erlang).
"""


def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""

    result = ""
    max_len = 0
    for i in range(0, len(strarr) - k + 1):
        current = "".join(strarr[i:i+k])
        current_len = len(current)
        if current_len > max_len:
            max_len = current_len
            result = current
    return result

print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2))