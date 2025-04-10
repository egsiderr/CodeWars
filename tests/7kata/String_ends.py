"""Дополните решение так, чтобы оно возвращало true,
если первый переданный аргумент (строка) заканчивается на 2-й аргумент (тоже строка).
Примеры:
solution('abc', 'bc') # возвращает true
solution('abc', 'd') # возвращает false"""


def solution(text, ending):
    return text.endswith(ending)

print(solution('abc', 'bc'))