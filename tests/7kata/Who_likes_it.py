"""Реализуйте функцию, которая принимает массив,
содержащий имена людей, которым понравился элемент.
Она должна возвращать отображаемый текст, как показано в примерах:
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"""

def likes(names):
    if names is None or len(names) == 0:
        return "no one likes this"

    if len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"

print(likes(["Max", "John", "Mark"]))