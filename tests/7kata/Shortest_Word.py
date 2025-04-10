"""Простой способ: задайте строку слов и верните длину самого короткого слова (слов).
Строка никогда не будет пустой, и вам не нужно учитывать различные типы данных."""

def find_short(s):
    shortest = (min(s.split(), key=len))
    return len(shortest)

print(find_short("dfdf fdfdfdfdf dfdfdfd"))