"""Заполните решение так, чтобы функция разбивала camel casing,
используя пробел между словами.

Пример
"camelCasing" => "camel Casing"
"identifier" => "identifier"
"" => """""

def solution(s):
    if not s:
        return ""

    result = ""
    for i, char in enumerate(s):
        if i > 0 and char.isupper():
            result += " "
        result += char
    return result

print(solution("camelCasing"))