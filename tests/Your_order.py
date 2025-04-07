"""Ваша задача - отсортировать заданную строку.
Каждое слово в строке будет содержать одно число.
Это число - позиция, которую слово должно занять в результате.
Примечание: Числа могут быть от 1 до 9. Поэтому 1 будет первым словом (а не 0).
Если входная строка пуста, возвращается пустая строка.
Слова во входной строке будут содержать только правильные последовательные числа.
Примеры
"is2 Thi1s T4est 3a" --> "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2" --> "Fo1r the2 g3ood 4of th5e pe6ople"
"" --> ""

Переведено с помощью DeepL.com (бесплатная версия)"""

def order(sentence):
    if sentence == "":
        return ""

    words = sentence.split()
    sorted_words = sorted(words, key=get_number)
    return " ".join(sorted_words)

def get_number(word):
    for i in word:
        if i.isdigit():
            return int(i)

print(order("is2 Thi1s T4est 3a"))
