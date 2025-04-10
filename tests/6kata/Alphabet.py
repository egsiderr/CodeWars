"""В этом ката вам нужно, получив строку, заменить каждую букву на ее место в алфавите.
Если что-то в тексте не является буквой, игнорируйте это и не возвращайте.
«a» = 1, «b» = 2 и т. д.
Пример
Вход = "Закат заходит в двенадцать часов".
Выход = «20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11»."""

def alphabet_position(text):
    # res = []
    # new_text = text.lower()
    # for i in new_text:
    #     if i.isalpha():
    #         res.append(ord(i) - 96)
    # res2 = ''
    # for x in res:
    #     res2 += str(x) + " "
    # return res2.strip()

    new_text = text.lower()
    res = ''
    for i in new_text:
        if i.isalpha():
            res = res + str(ord(i) - 96) + " "
    return res.strip()

print(alphabet_position('Afgdfg'))