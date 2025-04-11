"""Возвращает количество (count) гласных в заданной строке.
В этом Ката мы будем считать гласными буквы a, e, i, o, u (но не y).
Входная строка будет состоять только из строчных букв и/или пробелов."""

def get_count(sentence):
    count = 0
    glas = "aeiou"
    for i in sentence:
        if i in glas:
            count += 1
    return count
print(get_count('sfdsgdfgdfgasda'))